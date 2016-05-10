# -*- coding:utf8 -*-
'''
Main Form.
'''
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo, ValidationError
from ..models import Post
from flask.ext.pagedown.fields import PageDownField

class PostForm(Form):
    title = StringField('博文标题', validators=[Required(), Length(0, 120)])
    tags = StringField('博文标签', validators=[Required(), Length(0,120)])
    body = PageDownField('有什么好的想法？', validators=[Required()])
    submit = SubmitField('提交')

    def validate_tags(self, filed):
        tag_list = filed.data.split(';')
        for tag in tag_list:
            if len(tag) > 10:
                raise ValidationError('单个标签长度不得大于10字节。')
