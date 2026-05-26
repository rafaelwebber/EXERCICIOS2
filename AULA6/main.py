from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

#cria as tabelas caso nao exista
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.post('/estudantes/', response_model=schemas.EstudanteResponse)
def create_student(student: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_student = models.Estudante(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get('/estudante/{estudante_id}', response_model = schemas.EstudanteResponse)
def ler_estudante(estudante_id: int, db: Session = Depends(get_db)):
    estudante = db.query(models.Estudante).filter(models.Estudante.id == estudante_id).first()
    if estudante is None:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    return estudante


@app.get('/estudantes/', response_model = List[schemas.EstudanteResponse])
def read_students(db:Session = Depends(get_db)):
    students = db.query(models.Estudante).all()
    return students

@app.post('/matricula/', response_model=schemas.MatriculaResponse)
def create_matricula(matricula: schemas.MatriculaCreate, db:Session = Depends(get_db)):
    db_matriculas = models.Matricula(**matricula.model_dump())
    db.add(db_matriculas)
    db.commit()
    db.refresh(db_matriculas)
    return db_matriculas

@app.get('/matriculas/', response_model = List[schemas.MatriculaResponse])
def read_matriculas(db: Session = Depends(get_db)):
    matriculas = db.query(models.Matricula).all()
    return matriculas


