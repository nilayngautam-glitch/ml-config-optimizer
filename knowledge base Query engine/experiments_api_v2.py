from python_to_postgreSQL_model import ExperimentsBase, Experiment_insert, Experiment_update, Experiment
from fastapi import FastAPI, HTTPException, Query, Depends
from sqlmodel import SQLModel, Field, Session, select, create_engine

username = "postgres"
password = "nilay123"
host = "localhost"
port = 5432
database_name = "ml_configure_optimzer"
	
connection_str = f"postgresql://{username}:{password}@{host}:{port}/{database_name}"

engine = create_engine(connection_str)

SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI()

@app.post("/experiments")
async def insert(*, session : Session = Depends(get_session), exp : Experiment_insert):
    db_exp = Experiment.model_validate(exp)
    session.add(db_exp)
    session.commit()
    session.refresh(db_exp)
    return db_exp


@app.get("/experiments")
async def read_all(*, session: Session = Depends(get_session)):
    exps = session.exec(select(Experiment)).all()
    return exps

@app.get("/experiments/best")
async def best(*, session: Session = Depends(get_session)):
    best_exp = session.exec(select(Experiment).order_by(Experiment.val_accuracy.desc(), Experiment.val_loss.asc()).limit(1)).all()
    return best_exp