def up(db):
    db.notes.insert({'content': 'test'})
    db.notes.insert({'content2': 'test'})
    pass

def down(db):
    db.notes.remove({'content': 'test'})
