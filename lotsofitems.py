from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, User, Item

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

category1 = Category(user_id=1, name="Hocky")
session.add(category1)
session.commit()

item1 = Item(user_id=1, category=category1, name="Stick", description="Field hockey sticks have an end which varies in shape, often depending on the players position. In general there are four main variations on head:")
session.add(item1)
session.commit()

category2 = Category(user_id=1, name="Snowboarding")
session.add(category2)
session.commit()

item1 = Item(user_id=1, category=category2, name="Goggles", description="Goggles or safety glasses are forms of protective eyewear that usually enclose or protect the area surrounding the eye in order to prevent particulates, water or chemicals from striking the eyes. They are used in chemistry laboratories and in woodworking. They are often used in snow sports as well, and in swimming. Goggles are often worn when using power tools such as drills or chainsaws to prevent flying particles from damaging the eyes. Many types of goggles are available as prescription goggles for those with vision problems.")
session.add(item1)
session.commit()

item2 = Item(user_id=1, category=category2, name="Snowboard", description="Snowboards are boards that are usually the width of one's foot longways, with the ability to glide on snow.[1] Snowboards are differentiated from monoskis by the stance of the user. In monoskiing, the user stands with feet inline with direction of travel (facing tip of monoski/downhill) (parallel to long axis of board), whereas in snowboarding, users stand with feet transverse (more or less) to the longitude of the board. ")
session.add(item2)
session.commit()

print "added menu items!"