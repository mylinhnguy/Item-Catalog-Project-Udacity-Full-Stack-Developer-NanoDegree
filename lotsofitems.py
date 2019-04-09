from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut for easier to update database
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create the user
User1 = User(name="Linda Nguyen", email="linda.oc.oc@gmail.com")
session.add(User1)
session.commit()

# Create category of Women's Hair
category1 = Categories(user_id=1, name="Hairstyles for women")
session.add(category1)
session.commit()

# Create category of Men's Hair
category2 = Categories(user_id=1, name="Hairstyles for men")
session.add(category2)
session.commit()

# Create category of Bridal HeadPieces
category3 = Categories(user_id=1, name="Bridal HeadPieces")
session.add(category3)
session.commit()

# Add women face shape into category  
categoryItem1 = CategoryItem(user_id=1, name="Heart Face Shape",
                            description="The hairline is the widest part of the face. Narrow chin and prominent cheekbones.\
                            Best hairstyles for heart face shape are shoulder length lob, deep side part with loose waves, layers that break at the collarbone",
                            url_image="https://cdn.cliqueinc.com/cache/posts/227220/haircuts-for-heart-shaped-faces-227220-1497910280159-image.500x0c.jpg?interlace=true&quality=70",
							categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Round Face Shape",
                            description="Round face characteristics are width and length are the same. It is also known as a baby face.\
							Best hairstyles for round face shape are textured lob, deep side part, slick back, high ponytail, pixie cuts with volume at he top ",
                            url_image="http://www.zarias.com/wp-content/uploads/2015/10/3.jpg",
							categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Square Face Shape",
                             description="Square face characteristics are strong, angled jawline. Forehead, cheekbones, and jawline are the same width.\
							 Best hairstyles for square face shape are soft, wispy side-swept bangs, straight hair with long layers, short and subtle bangs that hit at the cheekbones ",
                             url_image="https://theskincareedit.com/.image/c_limit%2Ccs_srgb%2Cq_auto:good%2Cw_600/MTU2ODk4NjE4OTQ3MDg1OTM2/lucy-liu-square-face-bangs.webp",
							 categories=category1)
session.add(categoryItem1)
session.commit()


# Add men face shape into category
categoryItem1 = CategoryItem(user_id=1, name="Heart Face Shape",
                             description="Widest at the temples and tapering down to a point at the chin, heart-shaped faces are not the most common but can still be catered for with some clever barbering.\
                             Best hairstyles for heart face shape are length and volume on top, avoid very short styles, use facial hair to fill out the jawline",
                             url_image="https://www.zwivel.com/blog/wp-content/uploads/2017/11/Ryan-Gosling-e1510086929484.jpg",
							 categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Round Face Shape",
                             description="Wide cheeks and soft lines can work together to create a babyish look.\
							 Best hairstyles for round face shape use hair on top to create height,keep hair closely cropped at the back and sides ",
                             url_image="https://www.menshairstylestoday.com/wp-content/uploads/2016/05/Brad-Pitt-Undercut.jpg",
							 categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Square Face Shape",
                             description="Strong, angular jawline is no doubt one of your proudest features. But combined with the uniform width of your cheekbones and forehead, it can be quite a harsh overall look.\
							 Best hairstyles for square face shape use texture to soften lines, mid-length or short styles work best, use stubble to smooth harsh angles around the jaw ",
                             url_image="https://pauldeboer.info/wp-content/uploads/hairstyle-for-square-face-man-hairstyle-for-square-face-man-new-top-20-elegant-haircuts-for-guys-with-square-faces-1.jpg",
							 categories=category2)
session.add(categoryItem1)
session.commit()


# Add bridal hairpieces into category
categoryItem1 = CategoryItem(user_id=1, name="Heart Face Shape",
                             description="A heart shaped face is one that is wider at the temples and hairline, with the focal point at your pretty pointy chin.\
							 Position the piece above your ear or along your hairline. Position the piece near your temple to draw attention to your gorgeous cheekbones",   
                             url_image="https://i.pinimg.com/originals/2b/a2/9b/2ba29b92c6aa5260bffabfdc0016aa23.jpg",
							 categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Round Face Shape",
                             description="Use height to elongate the face and use pieces around the face to draw out cheekbones and slim. Avoid styles lacking in volume and height, piece with too much fullness at the sides ",
                             url_image="https://www.perfectweddingguide.com/wedding-blog/wp-content/uploads/2015/09/Best-Cannes-2012-65th-Annual-Cannes-Film-Festival-Nvk1uN4vIhbl-e1443451645780.jpg",
							 categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Square Face Shape",
                             description="Jaw is quite angular and is often slightly wider than your temples and hairline. Goal is to play down your angular jaw.\
							 Team up a headpiece with textured curls and a pretty side part. Choose a headpiece that you can wear near the temple to add length and to creates a pretty asymmetrical detail to soft the lines.",
                             url_image="http://img.everafterguide.net/s/upload/images/2016/05/e32bca46fe2f1f6c0657cd66efb620a5.jpg",
							 categories=category3)
session.add(categoryItem1) 
session.commit()


print "added items into catalog!"
