from fastapi import FastAPI, Response, HTTPException, Depends, status
from . import models, schemas
from sqlalchemy.orm import Session
from app.database import engine
from app.database import get_db


models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    tags=["Lawyer"]
)


@app.get("/law", status_code=status.HTTP_200_OK)
def get_all_firms(db: Session = Depends(get_db)):
    posts = db.query(models.Law_Firm).all()
    return posts


@app.post("/law", status_code=status.HTTP_201_CREATED)
def create_firm(firm: schemas.Add_Firm, db: Session = Depends(get_db)):
    new_firm = models.Law_Firm(**firm.dict())
    db.add(new_firm)
    db.commit()
    db.refresh(new_firm)
    return new_firm


@app.put("/law/{id}")
def update_firm(id: int, updated_firm: schemas.Update_Firm, db: Session = Depends(get_db)):
    firm_query = db.query(models.Law_Firm).filter(models.Law_Firm.id == id)
    post = firm_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"firm with id: {id} does not exist")
    firm_query.update(updated_firm.dict(), synchronize_session=False)
    db.commit()
    return firm_query.first()


@app.patch("/law/{id}")
def update_firm(id: int, updated_firm: schemas.UpdateHierarchy, db: Session = Depends(get_db)):
    firm_query = db.query(models.Law_Firm).filter(models.Law_Firm.id == id)
    post = firm_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"firm with id: {id} does not exist")
    firm_query.update(updated_firm.dict(), synchronize_session=False)
    db.commit()
    return (updated_firm)

@app.delete("/law/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_firm(id: int, db: Session= Depends(get_db)):
    firm = db.query(models.Law_Firm).filter(models.Law_Firm.id == id)
    if firm.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"firm with id: {id} was not found")
    firm.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_202_ACCEPTED)