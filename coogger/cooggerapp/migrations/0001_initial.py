# Generated by Django 2.0 on 2018-07-07 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djmd.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('icon_address', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Be sure to choose the best title related to your content.', max_length=100, verbose_name='Title')),
                ('permlink', models.SlugField(max_length=200)),
                ('content', djmd.models.EditorMdField()),
                ('tag', models.CharField(help_text='Write your tags using spaces,the first tag is your topic max:4 .', max_length=200, verbose_name='keyword')),
                ('category', models.CharField(blank=True, choices=[('science', 'science'), ('tutorial', 'tutorial'), ('idea', 'idea'), ('project', 'project'), ('computer', 'computer'), ('language', 'language'), ('art', 'art'), ('technology', 'technology'), ('biography', 'biography'), ('books', 'books'), ('business', 'business'), ('media', 'media'), ('travel', 'travel'), ('health', 'health'), ('music', 'music'), ('food', 'food'), ('history', 'history'), ('finance', 'finance'), ('exchange', 'exchange'), ('design-graphic', 'design-graphic'), ('development', 'development'), ('question-answer', 'question-answer'), ('translation', 'translation'), ('discussion', 'discussion')], help_text='select content category', max_length=30, null=True)),
                ('language', models.CharField(choices=[('turkish', 'turkish'), ('english', 'english'), ('korean', 'korean'), ('spanish', 'spanish'), ('arabic', 'arabic'), ('french', 'french'), ('portuguese', 'portuguese'), ('german', 'german'), ('italian', 'italian'), ('japanese', 'japanese'), ('romanian', 'romanian'), ('russian', 'russian'), ('vietnamese', 'vietnamese '), ('arabic', 'arabic'), ('azerbaijani', 'azerbaijani')], help_text='The language of your content', max_length=30)),
                ('definition', models.CharField(help_text='Briefly tell your readers about your content.', max_length=400, verbose_name='definition of content')),
                ('topic', models.CharField(help_text='Please, write your topic about your contents.', max_length=30, verbose_name='content topic')),
                ('status', models.CharField(choices=[('shared', 'shared'), ('changed', 'changed'), ('rejected', 'rejected'), ('approved', 'approved')], default='shared', max_length=30, verbose_name="content's status")),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
                ('dor', models.CharField(default=0, max_length=10)),
                ('views', models.IntegerField(default=0, verbose_name='views')),
                ('read', models.IntegerField(default=0, verbose_name='pageviews')),
                ('lastmod', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified date')),
                ('cooggerup', models.BooleanField(default=False, verbose_name='was voting done')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooggerapp.Community')),
                ('mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='moderator', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Contentviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooggerapp.Content')),
            ],
        ),
        migrations.CreateModel(
            name='OtherInformationOfUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', djmd.models.EditorMdField()),
                ('hmanycontent', models.IntegerField(default=0)),
                ('cooggerup_confirmation', models.BooleanField(default=False, verbose_name='Do you want to join in curation trails of the cooggerup bot with your account?')),
                ('cooggerup_percent', models.CharField(choices=[('100', '100'), ('99', '99'), ('98', '98'), ('97', '97'), ('96', '96'), ('95', '95'), ('94', '94'), ('93', '93'), ('92', '92'), ('91', '91'), ('90', '90'), ('89', '89'), ('88', '88'), ('87', '87'), ('86', '86'), ('85', '85'), ('84', '84'), ('83', '83'), ('82', '82'), ('81', '81'), ('80', '80'), ('79', '79'), ('78', '78'), ('77', '77'), ('76', '76'), ('75', '75'), ('74', '74'), ('73', '73'), ('72', '72'), ('71', '71'), ('70', '70'), ('69', '69'), ('68', '68'), ('67', '67'), ('66', '66'), ('65', '65'), ('64', '64'), ('63', '63'), ('62', '62'), ('61', '61'), ('60', '60'), ('59', '59'), ('58', '58'), ('57', '57'), ('56', '56'), ('55', '55'), ('54', '54'), ('53', '53'), ('52', '52'), ('51', '51'), ('50', '50'), ('49', '49'), ('48', '48'), ('47', '47'), ('46', '46'), ('45', '45'), ('44', '44'), ('43', '43'), ('42', '42'), ('41', '41'), ('40', '40'), ('39', '39'), ('38', '38'), ('37', '37'), ('36', '36'), ('35', '35'), ('34', '34'), ('33', '33'), ('32', '32'), ('31', '31'), ('30', '30'), ('29', '29'), ('28', '28'), ('27', '27'), ('26', '26'), ('25', '25'), ('24', '24'), ('23', '23'), ('22', '22'), ('21', '21'), ('20', '20'), ('19', '19'), ('18', '18'), ('17', '17'), ('16', '16'), ('15', '15'), ('14', '14'), ('13', '13'), ('12', '12'), ('11', '11'), ('10', '10'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1'), ('0', '0')], default=0, max_length=3)),
                ('vote_percent', models.CharField(choices=[('100', '100'), ('99', '99'), ('98', '98'), ('97', '97'), ('96', '96'), ('95', '95'), ('94', '94'), ('93', '93'), ('92', '92'), ('91', '91'), ('90', '90'), ('89', '89'), ('88', '88'), ('87', '87'), ('86', '86'), ('85', '85'), ('84', '84'), ('83', '83'), ('82', '82'), ('81', '81'), ('80', '80'), ('79', '79'), ('78', '78'), ('77', '77'), ('76', '76'), ('75', '75'), ('74', '74'), ('73', '73'), ('72', '72'), ('71', '71'), ('70', '70'), ('69', '69'), ('68', '68'), ('67', '67'), ('66', '66'), ('65', '65'), ('64', '64'), ('63', '63'), ('62', '62'), ('61', '61'), ('60', '60'), ('59', '59'), ('58', '58'), ('57', '57'), ('56', '56'), ('55', '55'), ('54', '54'), ('53', '53'), ('52', '52'), ('51', '51'), ('50', '50'), ('49', '49'), ('48', '48'), ('47', '47'), ('46', '46'), ('45', '45'), ('44', '44'), ('43', '43'), ('42', '42'), ('41', '41'), ('40', '40'), ('39', '39'), ('38', '38'), ('37', '37'), ('36', '36'), ('35', '35'), ('34', '34'), ('33', '33'), ('32', '32'), ('31', '31'), ('30', '30'), ('29', '29'), ('28', '28'), ('27', '27'), ('26', '26'), ('25', '25'), ('24', '24'), ('23', '23'), ('22', '22'), ('21', '21'), ('20', '20'), ('19', '19'), ('18', '18'), ('17', '17'), ('16', '16'), ('15', '15'), ('14', '14'), ('13', '13'), ('12', '12'), ('11', '11'), ('10', '10'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], default=100, max_length=3)),
                ('beneficiaries', models.CharField(choices=[('100', '100'), ('99', '99'), ('98', '98'), ('97', '97'), ('96', '96'), ('95', '95'), ('94', '94'), ('93', '93'), ('92', '92'), ('91', '91'), ('90', '90'), ('89', '89'), ('88', '88'), ('87', '87'), ('86', '86'), ('85', '85'), ('84', '84'), ('83', '83'), ('82', '82'), ('81', '81'), ('80', '80'), ('79', '79'), ('78', '78'), ('77', '77'), ('76', '76'), ('75', '75'), ('74', '74'), ('73', '73'), ('72', '72'), ('71', '71'), ('70', '70'), ('69', '69'), ('68', '68'), ('67', '67'), ('66', '66'), ('65', '65'), ('64', '64'), ('63', '63'), ('62', '62'), ('61', '61'), ('60', '60'), ('59', '59'), ('58', '58'), ('57', '57'), ('56', '56'), ('55', '55'), ('54', '54'), ('53', '53'), ('52', '52'), ('51', '51'), ('50', '50'), ('49', '49'), ('48', '48'), ('47', '47'), ('46', '46'), ('45', '45'), ('44', '44'), ('43', '43'), ('42', '42'), ('41', '41'), ('40', '40'), ('39', '39'), ('38', '38'), ('37', '37'), ('36', '36'), ('35', '35'), ('34', '34'), ('33', '33'), ('32', '32'), ('31', '31'), ('30', '30'), ('29', '29'), ('28', '28'), ('27', '27'), ('26', '26'), ('25', '25'), ('24', '24'), ('23', '23'), ('22', '22'), ('21', '21'), ('20', '20'), ('19', '19'), ('18', '18'), ('17', '17'), ('16', '16'), ('15', '15'), ('14', '14'), ('13', '13'), ('12', '12'), ('11', '11'), ('10', '10'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1'), ('0', '0')], default=0, max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReportModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaints', models.CharField(choices=[('fraud-or-plagiarism', 'fraud or plagiarism'), ('hate-speech-or-internet-trolling', 'hate speech or internet trolling'), ('intentional-miss-categorized-content-or-spam', 'intentional miss-categorized content or spam'), ('this-content-is-not-tutorial-content', 'this content is not tutorial content'), ('wrong-list-name', 'wrong list name'), ('i-think-this-content-should-not-be-at-coogger', 'i think this content should not be at coogger')], max_length=40, verbose_name='type of report')),
                ('add', models.CharField(blank=True, max_length=600, null=True, verbose_name='Can you give more information ?')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooggerapp.Content', verbose_name='şikayet edilen içerik')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='şikayet eden kişi')),
            ],
        ),
        migrations.CreateModel(
            name='SearchedWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=310, unique=True)),
                ('hmany', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.CharField(blank=True, choices=[('facebook', 'facebook'), ('instagram', 'instagram'), ('youtube', 'youtube'), ('github', 'github'), ('linkedin', 'linkedin'), ('web-site', 'web site')], max_length=15, null=True, verbose_name='website')),
                ('adress', models.CharField(blank=True, max_length=150, null=True, verbose_name='write address / username')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
