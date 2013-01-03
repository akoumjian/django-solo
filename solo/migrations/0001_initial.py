# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table('solo_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pubdate', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('body_markdown', self.gf('django.db.models.fields.TextField')()),
            ('body_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from=None, unique_with=())),
        ))
        db.send_create_signal('solo', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table('solo_post')


    models = {
        'solo.post': {
            'Meta': {'ordering': "('-pubdate',)", 'object_name': 'Post'},
            'body_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_markdown': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'pubdate': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['solo']