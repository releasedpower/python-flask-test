from app import db

class Region(db.Model):
    __tablename__ = 'region'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Region {self.name} ({self.id})>"
