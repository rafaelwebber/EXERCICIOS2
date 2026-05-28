from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal
from typing import List
from sqlalchemy.orm import joinedload

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/estudantes', response_model=schemas.Estudante)#response_model=schemas.Estudante validação para estudantes
def criar_estudante(estudante: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_estudante = models.Estudante(
        nome=estudante.nome,
        email=estudante.email,
        perfil=models.Perfil(**estudante.perfil.model_dump()),
    )
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante

@app.get('/estudantes/', response_model=List[schemas.Estudante])
def listar_estudantes(db: Session = Depends(get_db)):
    estudantes = db.query(models.Estudante).options(joinedload(models.Estudante.perfil)).all()
    return estudantes

#professores, matriculos e disciplinas 
@app.post('/professor', response_model=schemas.Professor)
def criar_professor(professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    db_professor = models.Professor(
        nome=professor.nome,
        email=professor.email,
    )
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor

@app.get('/professor', response_model=List[schemas.Professor])
def listar_professor(db: Session = Depends(get_db)):
    professores = db.query(models.Professor).options(joinedload(models.Professor.disciplinas)).all()
    return professores

@app.post('/disciplina', response_model=schemas.Disciplina)
def criar_disciplina(disciplina: schemas.DisciplinaCreate, db: Session = Depends(get_db)):
    db_disciplina = models.Disciplina(
        nome=disciplina.nome,
        professor_id=disciplina.professor_id,
    )
    db.add(db_disciplina)
    db.commit()
    db.refresh(db_disciplina)
    return (
        db.query(models.Disciplina)
        .options(joinedload(models.Disciplina.professor))
        .filter(models.Disciplina.id == db_disciplina.id)
        .first()
    )

@app.get('/disciplina', response_model=List[schemas.Disciplina])
def listar_disciplina(db: Session = Depends(get_db)):
    disciplinas = (
        db.query(models.Disciplina)
        .options(joinedload(models.Disciplina.professor))
        .all()
    )
    return disciplinas

@app.post('/matricula', response_model=schemas.Matricula)
def criar_matricula(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    db_matricula = models.Matricula(
        estudante_id=matricula.estudante_id,
        disciplina_id=matricula.disciplina_id,
    )
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula

@app.get('/matricula', response_model=List[schemas.Matricula])
def listar_matriculas(db: Session = Depends(get_db)):
    matriculas = (
        db.query(models.Matricula)
        .options(
            joinedload(models.Matricula.estudante),
            joinedload(models.Matricula.disciplina),
            )
        .all()
    )
    return matriculas
