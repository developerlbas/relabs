#encoding:utf-8
"""
Si el archivo no corresponde a los atributos:
1. content_type
2. charset
Lanzar la excepcion
UploadedFile objects
In addition to those inherited from File, all UploadedFile objects define the -
following methods/attributes:

UploadedFile.content_type
The content-type header uploaded with the file (e.g. text/plain or application-
/pdf). Like any data supplied by the user, you shouldn’t trust that the uploa--
ded file is actually this type. You will still need to validate that the file ---
contains the content that the content-type header claims – "trust but verify."

UploadedFile.charset
For text/* content-types, the character set (i.e. utf8) supplied by the browser.
Again, "trust but verify" is the best policy here.

UploadedFile.temporary_file_path
Only files uploaded onto disk will have this method; it returns the full path -
to the temporary uploaded file.
"""
class UnknownSource(Exception):
	msg = u"El archivo no puede ser procesado."
	
	def __init__(self, err=None):
		if err:
			self.msg = u"%(msg)s - error: %(err)s" % {'msg':self.msg, 'err':err}
