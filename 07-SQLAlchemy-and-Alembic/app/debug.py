
# 3.✅ CRUD practice
# To run the file run `python3 console.py` in the app directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Pet)

if __name__ == '__main__':
    #3.1 ✅ Uncomment bellow to create the engine
    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)


    #3.2 ✅ Uncomment bellow to create sessions and bind o the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    #session => Object to Run CRUD queries 


    #3.3 ✅  -- Creating records
    # Create a pet and save it to the data base with session.add and session.commit
    # honey = Pet(name = "Honey", species = "dog", breed = "poodle", temperament = "relaxed", owner_id=1)

    # to create one pet
    # session.add(honey)
    # session.commit()

    # Create multiple pets and bulk save them with  session.bulk_save_objects and session.commit
    honey = Pet(name = "Honey", species = "dog", breed = "poodle", temperament = "relaxed", owner_id=1)
    milk = Pet(name = "Milk", species = "dog", breed = "poodle", temperament = "tranquil", owner_id=2)
    happy = Pet(name = "Happy", species = "dog", breed = "poodle", temperament = "jazzed", owner_id=3)

    session.bulk_save_objects([honey, milk, happy])
    session.commit()
 


        #Note: bulk save will not contain the id

        #verify by checking the db 
    #3.4 ✅ Read
    # Get all with session.query
    pets = session.query(Pet)

    # Print the pets 
    print([pet for pet in pets])
    print("------------------------------------")

    #Get all of the pet names and print them with session.query
    print([pet.name for pet in pets])
    print("------------------------------------")

    names = [name for name in session.query(Pet.name)]
    print(names)
    print("------------------------------------")

    #Get all the pet names and print them in order with session.query and order_by
    name_in_order = [name for name in session.query(Pet.name).order_by(Pet.name)]
    print(name_in_order)
    print("------------------------------------")

    #Get the first pet with session.query and first
    first = session.query(Pet).first()
    print(first)
    print("------------------------------------")

    #Filter pet by temperament with session.query and filter 
    query = session.query(Pet).filter(Pet.temperament.like('%relaxed%'))
    for record in query:
        print(record)    
    print("------------------------------------")

    #3.5 ✅ Update 
        # Update the pets name and print the updated pet info
    first.name = "Joy"
    session.commit()
    print(first)
    print("------------------------------------")
        # Update all the pets temperament to 'cool' and print the pets 
    session.query(Pet).update({Pet.temperament: 'Cool'})
    pets = session.query(Pet)
    print([pet.temperament for pet in pets])
    print("------------------------------------")
    #3.6 ✅  Delete
        # Delete one item by querying the first pet, deleting it and committing it
    delete_this_pet = session.query(Pet).first()
    session.delete(delete_this_pet)
    session.commit()
    print([pet.id for pet in pets])
    print("------------------------------------")
    #delete all the pets with session.query and .delete
    # session.query(Pet).delete()
    # session.commit()
    print([pet for pet in pets])
    print("------------------------------------")
    # optional Break point for debugging and testing
    import ipdb; ipdb.set_trace()