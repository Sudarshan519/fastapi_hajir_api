from fastapi import HTTPException
from sqlmodel import SQLModel,Session


class RecordService(SQLModel):
    @classmethod
    def by_id(cls, id: int, session:Session):
        obj = session.get(cls, id)
        if obj is None:
            raise HTTPException(status_code=404, detail=f"{cls.__name__} with id {id} not found")
        return obj

    @classmethod
    def all(cls, session):
        return session. query(cls).limit(100).all()

    @classmethod
    def create(cls, source: dict  , SQLModel, session:Session):
        if isinstance(source, SQLModel):
            obj = cls.from_orm(source)
        elif isinstance(source, dict):
            obj = cls.parse_obj(source)
        session.add(obj)
        session.commit()
        session.refresh(obj)
 
        return obj

    def save(self, session:Session):
        session.add(self)
        session.commit()
        session.refresh(self)

    def update(self, source: dict| SQLModel, session:Session):
 
        if isinstance(source, SQLModel):
            source = source.dict(exclude_unset=True)

        for key, value in source.items():
            setattr(self, key, value)
        self.save(session)
        session.refresh(self)
        return self

    def delete(self, session:Session):
        session.delete(self)
        session.commit()
