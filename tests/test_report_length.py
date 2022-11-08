from lib.report_length import report_length

def length ():
    result = report_length("This is banana's!")
    assert result == 17