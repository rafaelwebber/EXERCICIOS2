from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Estudante(Base):
    __tablename__ = "estudantes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100))

    perfil = relationship(
        "Perfil",
        back_populates="estudante",
        uselist=False,
        cascade="all, delete-orphan",
    )
    matriculas = relationship("Matricula", back_populates="estudante")


class Perfil(Base):
    __tablename__ = "perfil"
    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String(200))
    estudante_id = Column(Integer, ForeignKey("estudantes.id"), unique=True)
    estudante = relationship("Estudante", back_populates="perfil")


class Professor(Base):
    __tablename__ = "professor"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100))

    disciplinas = relationship("Disciplina", back_populates="professor")


class Matricula(Base):
    __tablename__ = "matricula"
    id = Column(Integer, primary_key=True, index=True)
    estudante_id = Column(Integer, ForeignKey("estudantes.id"))
    disciplina_id = Column(Integer, ForeignKey("disciplina.id"))

    estudante = relationship("Estudante", back_populates="matriculas")
    disciplina = relationship("Disciplina", back_populates="matriculas")


class Disciplina(Base):
    __tablename__ = "disciplina"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    professor_id = Column(Integer, ForeignKey("professor.id"))

    professor = relationship("Professor", back_populates="disciplinas")
    matriculas = relationship("Matricula", back_populates="disciplina")
