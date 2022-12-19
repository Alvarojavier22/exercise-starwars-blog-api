from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    __tablename__="planets"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return '<planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Characters(db.Model):
    __tablename__ = "character"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return '<planets %r' % self.id

        def serialize(self):
            return {
                "id": self.id,
                "name": self.name
            }


class Favorites(db.Model):
    __tablename__ = "favorites"
    id=db.Column(db.Integer, primary_key=True)
    favorite_type=db.Column(db.String(100), nullable=False)
    favorite_id=db.Column(db.Integer, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    user=db.relationship(User)

    def serialize(self):
            return {
                "id": self.id,
                "type": self.favorite_type,
                "favorite_id": self.favorite_id
            }