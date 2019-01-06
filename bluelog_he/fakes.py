











from bluelog_he.extensions import db
from bluelog_he.models import Admin




def fake_admin():
    admin = Admin(
        username='admin',
        blog_title='Bluelog',
        blog_sub_title="No, I'm the real thing.",
        name='Mima Kirigoe',
        about='Um, l, Mima Kirigoe, had a fun time as a member of CHAM...'
    )
    db.session.add(admin)
    db.session.commit()
