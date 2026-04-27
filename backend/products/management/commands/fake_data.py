
from django.core.management.base import BaseCommand
from products.models import Category, Product
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate fake data for products'

    def handle(self, *args, **options):
        faker = Faker('fr_FR')

        # Create 5 categories
        categories = []
        for i in range(5):
            name = faker.word().capitalize()
            slug = faker.slug(name)
            categorie = Category.objects.create(name=name, slug=slug)
            categories.append(categorie)
            self.stdout.write(f'Created category with succes: {name}')

        # Create products
        for i in range(8):
            Product.objects.create(
                name=faker.sentence(nb_words=4).replace('.',''),
                description=faker.text(max_nb_chars=450),
                category=random.choice(categories),
                price=faker.random_number(digits=4),
                stock=faker.random_int(0, 100)
            )

        self.stdout.write(f'Product : {i+1} created with succes')