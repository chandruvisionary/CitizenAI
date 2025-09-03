from datetime import datetime
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    concerns = db.relationship('Concern', backref='author', lazy=True, cascade='all, delete-orphan')
    votes = db.relationship('Vote', backref='user', lazy=True, cascade='all, delete-orphan')
    comments = db.relationship('Comment', backref='author', lazy=True, cascade='all, delete-orphan')
    feedback_entries = db.relationship('Feedback', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.email}>'

class Concern(db.Model):
    __tablename__ = 'concerns'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(200), nullable=True)
    priority = db.Column(db.String(20), nullable=False, default='medium')  # low, medium, high, urgent
    status = db.Column(db.String(20), nullable=False, default='open')  # open, in_progress, resolved, closed
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    votes = db.relationship('Vote', backref='concern', lazy=True, cascade='all, delete-orphan')
    comments = db.relationship('Comment', backref='concern', lazy=True, cascade='all, delete-orphan')
    
    @property
    def vote_score(self):
        return self.upvotes - self.downvotes
    
    def __repr__(self):
        return f'<Concern {self.title}>'

class Vote(db.Model):
    __tablename__ = 'votes'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    concern_id = db.Column(db.Integer, db.ForeignKey('concerns.id'), nullable=False)
    vote_type = db.Column(db.String(10), nullable=False)  # 'upvote' or 'downvote'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Ensure one vote per user per concern
    __table_args__ = (db.UniqueConstraint('user_id', 'concern_id', name='unique_user_concern_vote'),)
    
    def __repr__(self):
        return f'<Vote {self.vote_type} by User {self.user_id} on Concern {self.concern_id}>'

class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    concern_id = db.Column(db.Integer, db.ForeignKey('concerns.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Comment by User {self.user_id} on Concern {self.concern_id}>'

class ChatSession(db.Model):
    __tablename__ = 'chat_sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    question = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', backref='chat_sessions')
    
    def __repr__(self):
        return f'<ChatSession {self.id} by User {self.user_id}>'

class Feedback(db.Model):
    __tablename__ = 'feedback'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    chat_session_id = db.Column(db.Integer, db.ForeignKey('chat_sessions.id'), nullable=True)
    question = db.Column(db.Text, nullable=False)
    feedback_text = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(20), nullable=False)  # positive, negative, neutral
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    chat_session = db.relationship('ChatSession', backref='feedback')
    
    def __repr__(self):
        return f'<Feedback {self.sentiment} by User {self.user_id}>'
