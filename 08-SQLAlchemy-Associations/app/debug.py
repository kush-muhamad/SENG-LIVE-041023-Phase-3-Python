from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Owner, Pet, Job, Handler)

if __name__ == '__main__':

    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)
   
    Session = sessionmaker(bind=engine)
    session = Session()

    #3✅ One to Many
    #Getting an owners pets
    #Use session.query and first to grab the first owner
    first_owner = session.query(Owner).first()
    #use session.query and filter_by to get the owners pets from Pet
    owners_pets = session.query(Pet).filter_by(id=first_owner.id)
    print("-----[one for one in owners_pets]-----")   
    print([one for one in owners_pets])
   
    #print out your owners pets
  

    #Getting a pets owner
    #Use session.query and first to grab the first pet
    first_pet = session.query(Pet).first()

    #Use session.query and filter_by to get the owner associated with this pet
    pets_owners = session.query(Owner).filter_by(id=first_pet.id)
    print("------[owner for owner in pets_owners]-----")
    print([owner for owner in pets_owners])
    

    #4✅ Head back to models to build out a Many to Many 
#--------------------------------------------

#6.✅ Many to Many 
    #Use session.query and .first to get the first handler
    handler = session.query(Handler).first()

    #Use session.query and the .filter_by to grab the jobs
    handler_jobs = session.query(Job).filter_by(handler_id=handler.id)
    #Print the jobs
    print("---------[ job for job in handler_jobs]------")    
    print([ job for job in handler_jobs])
 
    #Use the handler_jobs to query pets for the associated pet to each job.
    handlers_pets = [session.query(Pet).get(job.pet_id) for job in handler_jobs]
    print("------handlers_pets-----")
    print(handlers_pets)

    #Optional breakpoint for debugging
    import ipdb; ipdb.set_trace()