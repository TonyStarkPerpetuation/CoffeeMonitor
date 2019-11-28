# Generated by Django 2.0 on 2019-04-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EqInfo',
            fields=[
                ('machine_id', models.AutoField(primary_key=True, serialize=False, verbose_name='设备编号')),
                ('category_id', models.IntegerField(verbose_name='设备类型')),
                ('name', models.CharField(default='', max_length=64, verbose_name='设备名称')),
                ('mac_addr', models.CharField(default='', max_length=64, verbose_name='网卡地址')),
                ('addr', models.CharField(default='', max_length=128, verbose_name='地址')),
                ('position', models.CharField(default='', max_length=64, verbose_name='位置')),
                ('install_date', models.DateField(verbose_name='安装日期')),
                ('install_emp_id', models.CharField(default='', max_length=16, verbose_name='安装人员')),
                ('status', models.IntegerField(verbose_name='设备状态')),
                ('mantain_emp_id', models.CharField(default='', max_length=16, verbose_name='运维人员')),
            ],
            options={
                'verbose_name': '设备信息',
                'verbose_name_plural': '设备信息',
            },
        ),
        migrations.CreateModel(
            name='EqState',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('machine_id', models.IntegerField(verbose_name='设备编号')),
                ('recv_time', models.DateTimeField(verbose_name='状态上报时间')),
                ('enviroment_temperature', models.CharField(default='', max_length=16, verbose_name='工作环境温度')),
                ('boiler_temperature', models.CharField(default='', max_length=16, verbose_name='锅炉温度')),
                ('boiler_pressue', models.CharField(default='', max_length=16, verbose_name='锅炉压力')),
                ('material_remainder', models.CharField(default='', max_length=16, verbose_name='配料桶余料')),
                ('orders_num', models.IntegerField(verbose_name='订单数量')),
                ('orders_amt', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='订单总金额')),
            ],
            options={
                'verbose_name': '设备状态',
                'verbose_name_plural': '设备状态',
            },
        ),
        migrations.CreateModel(
            name='EqType',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False, verbose_name='类型编号')),
                ('name', models.CharField(default='', max_length=64, verbose_name='类型名称')),
                ('size', models.CharField(default='', max_length=64, verbose_name='尺寸')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='重量')),
                ('power', models.CharField(default='', max_length=32, verbose_name='重量')),
                ('dissipation', models.IntegerField(verbose_name='功率')),
                ('material_buckets', models.IntegerField(verbose_name='配料桶数')),
                ('water_proofing_grade', models.CharField(default='', max_length=16, verbose_name='防水级别')),
                ('pipe_standard', models.CharField(default='', max_length=16, verbose_name='水管标准')),
                ('inflow_pressue', models.CharField(default='', max_length=16, verbose_name='供水压力')),
                ('work_temperature', models.CharField(default='', max_length=16, verbose_name='工作温度')),
                ('screen_size', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='屏幕尺寸')),
                ('comm_interface', models.CharField(default='', max_length=32, verbose_name='通信接口')),
                ('os', models.CharField(default='', max_length=32, verbose_name='操作系统')),
                ('payment_cate', models.CharField(default='', max_length=32, verbose_name='支付类型')),
                ('data_standard', models.CharField(default='', max_length=32, verbose_name='数据标准')),
            ],
            options={
                'verbose_name': '设备类型信息',
                'verbose_name_plural': '设备类型信息',
            },
        ),
        migrations.CreateModel(
            name='EqWarning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_id', models.IntegerField(verbose_name='设备编号')),
                ('alter_msg', models.CharField(default='', max_length=128, verbose_name='异常信息')),
                ('check_time', models.DateTimeField(verbose_name='异常发现时间')),
            ],
            options={
                'verbose_name': '设备报警',
                'verbose_name_plural': '设备报警',
            },
        ),
    ]