from sqlalchemy.exc import IntegrityError


def get_one_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).one_or_none()
    if instance:
        return instance, False
    else:
        instance = model(**kwargs)
        try:
            session.add(instance)
            session.commit()
        except IntegrityError:
            session.rollback()
            instance = session.query(model).filter_by(**kwargs).one()
            return instance, False
        else:
            return instance, True
