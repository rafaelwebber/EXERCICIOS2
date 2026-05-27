from typing import List, Optional
from pydantic import BaseModel

class Perfil(BaseModel):
    id: int
    idade: int
    endereco: str

    class Config:
        from_attributes = True

class PerfilCreate(BaseModel):
    idade: int
    endereco: str

class Estudante(BaseModel):
    id: int
    nome: str
    email: str
    perfil: Optional[Perfil] = None

    class Config: 
        from_attributes = True

class EstudanteCreate(BaseModel):
    nome: str
    email: str
    perfil: PerfilCreate

class DisciplinaResumo(BaseModel):
    nome: str

    class Config:
        from_attributes = True


class ProfessorResumo(BaseModel):
    nome: str

    class Config:
        from_attributes = True


class Professor(BaseModel):
    id: int
    nome: str
    email: str
    disciplinas: List[DisciplinaResumo] = []

    class Config:
        from_attributes = True


class ProfessorCreate(BaseModel):
    nome: str
    email: str


class Disciplina(BaseModel):
    id: int
    nome: str
    professor: Optional[ProfessorResumo] = None

    class Config:
        from_attributes = True

class DisciplinaCreate(BaseModel):
    nome: str
    professor_id : int

class Matricula(BaseModel):
    estudante_id : int
    disciplina_id : int

    class Config: 
        from_attributes = True

class MatriculaCreate(BaseModel):
    id: int
    estudante_id : int
    disciplina_id: int