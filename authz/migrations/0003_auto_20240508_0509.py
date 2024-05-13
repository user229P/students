from django.db import migrations


def add_default_courses(apps, schema_editor):
    Course = apps.get_model('authz', 'Course')

    # Add 10 courses
    Course.objects.bulk_create([
        Course(c_title='Introduction to Python Programming',
               c_description='This course covers the fundamentals of Python programming. '
                             'Topics include data types, control structures, functions, '
                             'file handling, and more. Students will gain hands-on experience '
                             'through programming assignments and projects.', 
               c_price=99.99,
               c_instructor='Sheldon Cooper'),
        Course(c_title='Web Development with Django',
               c_description='This course teaches web development using the Django framework. '
                             'Students will learn to build dynamic web applications with Django, '
                             'covering topics such as models, views, templates, forms, authentication, '
                             'and deployment.', 
               c_price=129.99,
               c_instructor='Raj Kumar'),
        Course(c_title='Machine Learning Fundamentals',
               c_description='This course introduces the basics of machine learning. '
                             'Topics include supervised learning, unsupervised learning, '
                             'regression, classification, clustering, and evaluation metrics. '
                             'Students will implement machine learning algorithms using Python '
                             'libraries such as scikit-learn.', 
               c_price=149.99,
               c_instructor='Michael Scott'),
        Course(c_title='Data Science Essentials',
               c_description='This course covers essential concepts and techniques '
                             'in data science. Topics include data preprocessing, '
                             'exploratory data analysis, feature engineering, '
                             'and predictive modeling. Students will work with real-world datasets '
                             'to solve practical data science problems.', 
               c_price=159.99,
               c_instructor='Pam Beesley'),
        Course(c_title='Advanced Algorithms and Data Structures',
               c_description='This course explores advanced algorithms and data structures '
                             'used in computer science. Topics include graph algorithms, '
                             'dynamic programming, greedy algorithms, advanced sorting, '
                             'and more. Students will analyze algorithm efficiency and '
                             'solve complex problems.', 
               c_price=179.99,
               c_instructor='Dwight SChrute'),
        Course(c_title='Cybersecurity Fundamentals',
               c_description='This course provides an overview of cybersecurity fundamentals. '
                             'Topics include network security, cryptography, '
                             'secure coding practices, threat modeling, and incident response. '
                             'Students will learn to identify and mitigate common security risks.', 
               c_price=139.99,
               c_instructor='Ted Mosby'),
        Course(c_title='Cloud Computing Essentials',
               c_description='This course introduces the essentials of cloud computing. '
                             'Topics include cloud service models, deployment models, '
                             'virtualization, containerization, and cloud security. '
                             'Students will gain practical experience with cloud platforms '
                             'such as AWS, Azure, and Google Cloud.', 
               c_price=169.99,
               c_instructor='Robin Green'),
        Course(c_title='Mobile App Development with React Native',
               c_description='This course teaches mobile app development using React Native. '
                             'Students will learn to build cross-platform mobile applications '
                             'for iOS and Android using JavaScript and React. Topics include '
                             'UI components, navigation, state management, and API integration.', 
               c_price=149.99,
               c_instructor='Chandler Bing'),
        Course(c_title='Blockchain Fundamentals',
               c_description='This course covers the fundamentals of blockchain technology. '
                             'Topics include decentralized networks, consensus mechanisms, '
                             'smart contracts, cryptocurrencies, and applications of blockchain. '
                             'Students will understand the underlying principles and architecture '
                             'of blockchain systems.', 
               c_price=189.99,
               c_instructor='Ross Geller'),
        Course(c_title='Artificial Intelligence and Ethics',
               c_description='This course explores the ethical implications of artificial intelligence. '
                             'Topics include bias in AI algorithms, data privacy, '
                             'ethical decision-making in AI development, '
                             'and societal impact of AI technologies. '
                             'Students will examine case studies and ethical frameworks.', 
               c_price=159.99,
               c_instructor='Rachel Green'),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('authz', '0002_course'),
    ]

    operations = [
        migrations.RunPython(add_default_courses),
    ]
