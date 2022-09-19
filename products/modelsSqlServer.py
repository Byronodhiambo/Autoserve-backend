from django.db import models

class Principalcompanymaster(models.Model):
    principalcompanyid = models.IntegerField(primary_key=True)
    principalcompanyname = models.CharField(unique=True, max_length=50)
    isactive_3 = models.BooleanField()
    isfixed_4 = models.BooleanField()
    mlnumber_5 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'principalcompanymaster'
        
class Brandmaster(models.Model):
    brandid_1 = models.IntegerField(primary_key=True)
    brandname = models.CharField(unique=True, max_length=50)
    principalcompanyid = models.ForeignKey('Principalcompanymaster', models.DO_NOTHING, db_column='principalcompanyid')
    areaallotted = models.DecimalField(max_digits=18, decimal_places=0)
    isfixed_5 = models.BooleanField()
    isactive_6 = models.BooleanField()
    spcommpercent = models.DecimalField(max_digits=5, decimal_places=2)
    spcommamt = models.DecimalField(max_digits=14, decimal_places=3)
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'brandmaster'

class Departmentmaster(models.Model):
    departmentid = models.IntegerField(primary_key=True)
    departmentname = models.CharField(unique=True, max_length=50)
    areaallotted = models.DecimalField(max_digits=18, decimal_places=0)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'departmentmaster'

class Productgroupmaster(models.Model):
    productgroupid = models.IntegerField(primary_key=True)
    productgroupname = models.CharField(unique=True, max_length=50)
    departmentid = models.ForeignKey(Departmentmaster, models.DO_NOTHING, db_column='departmentid')
    areaallotted = models.DecimalField(max_digits=18, decimal_places=0)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'productgroupmaster'


class Formatmaster(models.Model):
    formatid = models.SmallIntegerField(primary_key=True)
    formattype = models.CharField(max_length=50)
    vbprefix = models.CharField(max_length=50)
    vbsuffix = models.CharField(max_length=50)
    sqlprefix = models.CharField(max_length=50)
    sqlsuffix = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'formatmaster'

class Listmaster(models.Model):
    listid = models.SmallIntegerField(primary_key=True)
    listname = models.CharField(unique=True, max_length=35)
    isfixed = models.BooleanField()
    isactive = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'listmaster'

class Datatypemaster(models.Model):
    datatypeid = models.SmallIntegerField(primary_key=True)
    datatypename = models.CharField(unique=True, max_length=100)
    datatypeformat = models.CharField(max_length=20)
    display = models.CharField(max_length=15)
    prefixsuffix = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'datatypemaster'

class Matrixmaster(models.Model):
    matrixid = models.SmallIntegerField(primary_key=True)
    matrixname = models.CharField(unique=True, max_length=50)
    field1name = models.CharField(max_length=35)
    field1listid = models.ForeignKey(Listmaster, models.DO_NOTHING, db_column='field1listid_4', related_name='field1listid_4')
    field2name = models.CharField(max_length=35)
    field2listid = models.ForeignKey(Listmaster, models.DO_NOTHING, db_column='field2listid_6',  related_name='field2listid_6')
    field3name = models.CharField(max_length=35)
    field3listid = models.ForeignKey(Listmaster, models.DO_NOTHING, db_column='field3listid', related_name='field3listid')
    field4name = models.CharField(max_length=35)
    field4datatypeid = models.ForeignKey(Datatypemaster, models.DO_NOTHING, db_column='field4datatypeid', related_name='field4datatypeid')
    field5name = models.CharField(max_length=35)
    field5datatypeid = models.ForeignKey(Datatypemaster, models.DO_NOTHING, db_column='field5datatypeid', related_name='field5datatypeid')
    field6name = models.CharField(max_length=35)
    field6datatypeid = models.ForeignKey(Datatypemaster, models.DO_NOTHING, db_column='field6datatypeid', related_name='field6datatypeid')
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    linkfieldname = models.CharField(max_length=35)
    activateexpiry = models.SmallIntegerField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'matrixmaster'


class Subgroupmaster(models.Model):
    subgroupid = models.IntegerField(primary_key=True)
    subgroupname = models.CharField(unique=True, max_length=50)
    productgroupid = models.ForeignKey(Productgroupmaster, models.DO_NOTHING, db_column='productgroupid')
    matrixid = models.ForeignKey(Matrixmaster, models.DO_NOTHING, db_column='matrixid')
    taxidsale = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxidsale',  related_name='subgroupmastertaxidsale')
    taxidpurchase = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxidpurchase')
    areaallotted = models.DecimalField(max_digits=18, decimal_places=0)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    spcommpercent = models.DecimalField(max_digits=5, decimal_places=2)
    spcommamt = models.DecimalField(max_digits=14, decimal_places=3)
    mlnumber = models.BigIntegerField()
    taxslabsale = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'subgroupmaster'


class Hsnsacmaster(models.Model):
    hsnsacid = models.IntegerField(primary_key=True)
    hsnsaccode = models.CharField(unique=True, max_length=20)
    hsnsacname = models.CharField(max_length=50)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    mlnumber = models.BigIntegerField()
    uqc = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'hsnsacmaster'


class Unitmaster(models.Model):
    unitid = models.SmallIntegerField(primary_key=True)
    unitname = models.CharField(unique=True, max_length=20)
    formalname = models.CharField(max_length=25)
    digitafterdecimal = models.SmallIntegerField()
    conversionunit = models.SmallIntegerField()
    conversionqty = models.DecimalField(max_digits=13, decimal_places=3)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    mlnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'unitmaster'


class Taxmaster(models.Model):
    taxid = models.SmallIntegerField(primary_key=True)
    taxname = models.CharField(unique=True, max_length=50)
    includeinrate = models.BooleanField()
    taxvalue = models.DecimalField(max_digits=13, decimal_places=3)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    calcmethod = models.SmallIntegerField()
    loguser = models.SmallIntegerField()
    loglocation = models.SmallIntegerField()
    logsession = models.CharField(max_length=6)
    mlnumbe = models.BigIntegerField()
    interstatetaxid = models.SmallIntegerField()
    saleaccountid = models.IntegerField()
    salereturnaccountid = models.IntegerField()
    purchaseaccountid = models.IntegerField()
    purchasereturnaccountid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taxmaster'


class Productmaster(models.Model):
    productid = models.CharField(primary_key=True, max_length=4)
    productname = models.CharField(unique=True, max_length=50, blank=True, null=True)
    printname = models.CharField(max_length=50, blank=True, null=True)
    upcean = models.CharField(unique=True, max_length=20)
    userdefinedcode = models.CharField(max_length=16)
    maxretailprice = models.DecimalField(max_digits=14, decimal_places=3)
    brandid = models.ForeignKey(Brandmaster, models.DO_NOTHING, db_column='brandid')
    subgroupid = models.ForeignKey('Subgroupmaster', models.DO_NOTHING, db_column='subgroupid')
    productgroupid = models.ForeignKey(Productgroupmaster, models.DO_NOTHING, db_column='productgroupid')
    departmentid = models.ForeignKey(Departmentmaster, models.DO_NOTHING, db_column='departmentid')
    unitid = models.ForeignKey('Unitmaster', models.DO_NOTHING, db_column='unitid')
    binlocation = models.CharField(max_length=10)
    matrixid = models.ForeignKey(Matrixmaster, models.DO_NOTHING, db_column='matrixid')
    evalcount = models.IntegerField()
    taxidpurchase = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxidpurchase', related_name='taxidpurchase')
    taxidsale = models.ForeignKey('Taxmaster', models.DO_NOTHING, db_column='taxidsale', related_name='taxidsale')
    printbarcode = models.BooleanField()
    askrate = models.BooleanField()
    usefifo = models.BooleanField()
    productmessage = models.CharField(max_length=255)
    quantityonhand = models.DecimalField(max_digits=13, decimal_places=3)
    reorderinformation = models.BooleanField()
    reorderlevel = models.DecimalField(max_digits=13, decimal_places=3)
    safetylevel = models.DecimalField(max_digits=13, decimal_places=3)
    reorderquantity = models.DecimalField(max_digits=13, decimal_places=3)
    minimumorderquantity = models.DecimalField(max_digits=13, decimal_places=3)
    standardsaleprice = models.DecimalField(max_digits=14, decimal_places=3)
    standardcostprice = models.DecimalField(max_digits=14, decimal_places=3)
    productdiscount = models.DecimalField(max_digits=5, decimal_places=2)
    allowoperatordiscount = models.BooleanField()
    productremarks = models.CharField(max_length=255)
    picture1 = models.CharField(max_length=500)
    picture2 = models.CharField(max_length=500)
    recipecomponents = models.BooleanField()
    recorddatetime = models.DateTimeField()
    companyid = models.SmallIntegerField()
    sessionid = models.CharField(max_length=6)
    isactive = models.BooleanField()
    isfixed = models.BooleanField()
    conversionfactor = models.DecimalField(max_digits=13, decimal_places=3)
    alternateunitid = models.SmallIntegerField()
    changeconversion = models.BooleanField()
    itemtype = models.ForeignKey(Formatmaster, models.DO_NOTHING, db_column='itemtype')
    weighingscaleexport = models.BooleanField()
    weighingscaleconversion = models.IntegerField()
    printnameother = models.CharField(max_length=35)
    generateproductchild = models.SmallIntegerField()
    couponfile = models.CharField(max_length=500)
    spcommpercent = models.DecimalField(max_digits=5, decimal_places=2)
    spcommamt = models.DecimalField(max_digits=14, decimal_places=3)
    schemeids = models.CharField(max_length=250)
    pmfield1 = models.CharField(max_length=50)
    pmfield2 = models.CharField(max_length=50)
    pmfield3 = models.CharField(max_length=50)
    pmfield4 = models.CharField(max_length=50)
    pmfield5 = models.CharField(max_length=50)
    pmfield6 = models.CharField(max_length=50)
    pmfield7 = models.CharField(max_length=50)
    pmfield8 = models.CharField(max_length=50)
    pmfield9 = models.CharField(max_length=50)
    pmfield10 = models.CharField(max_length=50)
    calcnetweight = models.BooleanField()
    barcoderatio = models.DecimalField(max_digits=6, decimal_places=2)
    link = models.CharField(max_length=512)
    askquantity = models.SmallIntegerField()
    askcontainer = models.SmallIntegerField()
    serviceitem = models.CharField(max_length=4)
    rate = models.DecimalField(max_digits=14, decimal_places=3)
    periodicity = models.SmallIntegerField()
    upcean1 = models.CharField(unique=True, max_length=20)
    upcean2 = models.CharField(unique=True, max_length=20)
    upcean3 = models.CharField(unique=True, max_length=20)
    upcean4 = models.CharField(unique=True, max_length=20)
    teamid = models.CharField(max_length=50)
    changecontainerweight = models.SmallIntegerField()
    saleaccountid = models.IntegerField()
    salereturnaccountid = models.IntegerField()
    purchaseaccountid = models.IntegerField()
    purchasereturnaccountid = models.IntegerField()
    taxablevalue = models.DecimalField(max_digits=14, decimal_places=3)
    loguser = models.SmallIntegerField()
    loglocation = models.SmallIntegerField()
    logsession = models.CharField(max_length=6)
    webgroupid = models.SmallIntegerField()
    websubgroupid = models.SmallIntegerField()
    webitemname = models.CharField(max_length=500)
    isrecommended = models.SmallIntegerField()
    foodtype = models.SmallIntegerField()
    spicelevel = models.SmallIntegerField()
    webproductname = models.CharField(max_length=50)
    convertproductid = models.CharField(max_length=4)
    convertqty = models.DecimalField(max_digits=13, decimal_places=3)
    mlnumber = models.BigIntegerField()
    hsnsacid = models.ForeignKey(Hsnsacmaster, models.DO_NOTHING, db_column='hsnsacid', related_name='productmasterhsnsacid')
    productcodesap = models.CharField(max_length=50)
    generateproduction = models.SmallIntegerField()
    spcommdatewise = models.CharField(max_length=1000)
    sacid = models.ForeignKey(Hsnsacmaster, models.DO_NOTHING, db_column='sacid', related_name='productmastersacid')

    class Meta:
        managed = False
        db_table = 'productmaster'