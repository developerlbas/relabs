# Create your views here.
"""
Like regular Python files, you can read the file line-by-line simply
by iterating over the uploaded file:
for line in uploadedfile:
    do_something_with(line)
However, unlike standard Python files, UploadedFile only understands
\n (also known as -Unix-style-) line endings. If you know that you -
need to handle uploaded files with different line endings, you’ll --
need to do so in your view.

UploadedFile objects
In addition to those inherited from File, all UploadedFile objects -
define the following methods/attributes:

UploadedFile.content_type
The content-type header uploaded with the file (e.g. text/plain or -
application/pdf). Like any data supplied by the user, you shouldn’t 
trust that the uploaded file is actually this type. You’ll still need 
to validate that the file contains the content that the content-type
header claims – “trust but verify.”

UploadedFile.charset
For text/* content-types, the character set (i.e. utf8) supplied by -
the browser. Again, “trust but verify” is the best policy here.

UploadedFile.temporary_file_path
Only files uploaded onto disk will have this method; it returns the -
full path to the temporary uploaded file.
"""
