from django.test import TestCase
from django.utils import timezone
from .models import Auction, Artwork, Customer, Bid, Admin
from datetime import datetime

class ModelTests(TestCase):
    def test_models(self):
        # Crear instancias de cada modelo
        start_date = timezone.make_aware(datetime(2024, 4, 30, 12, 0, 0))
        end_date = timezone.make_aware(datetime(2024, 5, 1, 12, 0, 0))
        bid_timestamp = timezone.make_aware(datetime(2024, 4, 30, 13, 0, 0))

        auction = Auction.objects.create(
            auction_name="Subasta de prueba",
            auction_description="Descripción de la subasta",
            start_date=start_date,
            end_date=end_date,
            status="active"
        )

        artwork = Artwork.objects.create(
            auction=auction,
            title="Obra de arte de prueba",
            artist="Artista de prueba",
            year_created=2020,
            dimensions="10x10",
            material="Material de prueba",
            genre="Género de prueba",
            description="Descripción de la obra de arte de prueba",
            minimum_bid=10.00,
            status="active"
        )

        customer = Customer.objects.create(
            full_name="Cliente de prueba",
            email="cliente@example.com",
            phone="123456789",
            document_type="Tipo de documento",
            document_number="12345678"
        )

        bid = Bid.objects.create(
            auction=auction,
            artwork=artwork,
            customer=customer,
            bid_value=15.00,
            bid_timestamp=bid_timestamp
        )

        admin = Admin.objects.create(
            email="admin@example.com",
            password="password"
        )

        # Aserciones simples para verificar que se hayan creado instancias de cada modelo
        self.assertEqual(Auction.objects.count(), 1)
        self.assertEqual(Artwork.objects.count(), 1)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Bid.objects.count(), 1)
        self.assertEqual(Admin.objects.count(), 1)
