# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Student.exam_roll'
        db.add_column('profiles_student', 'exam_roll',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.sex'
        db.add_column('profiles_student', 'sex',
                      self.gf('django.db.models.fields.CharField')(default='M', max_length=1),
                      keep_default=False)


        # Changing field 'Student.group'
        db.alter_column('profiles_student', 'group', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Student.email'
        db.alter_column('profiles_student', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True))

        # Changing field 'Student.phone'
        db.alter_column('profiles_student', 'phone', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Student.exam_roll'
        db.delete_column('profiles_student', 'exam_roll')

        # Deleting field 'Student.sex'
        db.delete_column('profiles_student', 'sex')


        # Changing field 'Student.group'
        db.alter_column('profiles_student', 'group', self.gf('django.db.models.fields.CharField')(default=1, max_length=1))

        # Changing field 'Student.email'
        db.alter_column('profiles_student', 'email', self.gf('django.db.models.fields.EmailField')(default='ak@amity.edu', max_length=75))

        # Changing field 'Student.phone'
        db.alter_column('profiles_student', 'phone', self.gf('django.db.models.fields.IntegerField')(default=9))

    models = {
        'academics.course': {
            'Meta': {'object_name': 'Course'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'academics.section': {
            'Meta': {'object_name': 'Section'},
            'batch': ('django.db.models.fields.IntegerField', [], {}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['academics.Course']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profiles.faculty': {
            'Meta': {'object_name': 'Faculty'},
            'empID': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'profiles.student': {
            'Meta': {'object_name': 'Student'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academics.Course']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'enrolment_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'exam_roll': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'form_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academics.Section']"}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['profiles']