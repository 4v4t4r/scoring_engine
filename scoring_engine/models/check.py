from sqlalchemy import Column, Integer, ForeignKey, Boolean, String
from sqlalchemy.orm import relationship

from scoring_engine.models.base import Base


class Check(Base):
    __tablename__ = "checks"
    id = Column(Integer, primary_key=True)
    round_id = Column(Integer, ForeignKey('rounds.id'))
    round = relationship("Round", back_populates="checks")
    service_id = Column(Integer, ForeignKey('services.id'))
    service = relationship("Service")
    result = Column(Boolean)
    output = Column(String)