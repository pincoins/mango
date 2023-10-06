# Generated by Django 4.2.6 on 2023-10-06 15:14

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('description', models.TextField(blank=True)),
                ('sub_description', models.TextField(blank=True)),
                ('discount_rate', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('fullname', models.CharField(blank=True, max_length=64)),
                ('user_agent', models.TextField(blank=True)),
                ('accept_language', models.TextField(blank=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('payment_method', models.IntegerField(db_index=True)),
                ('transaction_id', models.CharField(blank=True, max_length=64)),
                ('status', models.IntegerField(db_index=True)),
                ('visible', models.IntegerField(db_index=True)),
                ('total_list_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('total_selling_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('message', models.TextField(blank=True)),
                ('suspicious', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
            ],
            options={
                'verbose_name': 'pincoin order',
                'verbose_name_plural': 'pincoin orders',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('list_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('selling_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('quantity', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
            ],
            options={
                'verbose_name': 'order product',
                'verbose_name_plural': 'order products',
                'db_table': 'order_product',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('code', models.SlugField(allow_unicode=True, max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('position', models.IntegerField()),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('stock_quantity', models.IntegerField(default=0)),
                ('minimum_stock_level', models.IntegerField(default=0)),
                ('maximum_stock_level', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=150, unique=True)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'role',
                'verbose_name_plural': 'roles',
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('code', models.CharField(max_length=64)),
                ('remarks', models.CharField(blank=True, max_length=64)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.product')),
            ],
            options={
                'verbose_name': 'voucher',
                'verbose_name_plural': 'vouchers',
                'db_table': 'voucher',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('password', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.role')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='OrderProductVoucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('code', models.CharField(max_length=64)),
                ('revoked', models.BooleanField(default=False)),
                ('remarks', models.CharField(blank=True, max_length=64)),
                ('order_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.orderproduct')),
                ('voucher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.voucher')),
            ],
            options={
                'verbose_name': 'order product voucher',
                'verbose_name_plural': 'order product vouchers',
                'db_table': 'order_product_voucher',
            },
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('account', models.IntegerField(db_index=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('balance', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=11)),
                ('received', models.DateTimeField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
            ],
            options={
                'verbose_name': 'order payment',
                'verbose_name_plural': 'order payments',
                'db_table': 'order_payment',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.user'),
        ),
        migrations.AddIndex(
            model_name='voucher',
            index=models.Index(fields=['code'], name='voucher_code_8bda2a_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='voucher',
            unique_together={('product', 'code')},
        ),
    ]
