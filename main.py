import csv
import sys
import lib.dns as dns
import lib.files as files

def main(fname):
  iocs = {}

  with open(fname) as ioc_file:
    csv_rdr = csv.reader(ioc_file)
    fields = next(csv_rdr)

    for row in csv_rdr:
      type = row[fields.index('type')]

      if iocs.get(type) != None:
        iocs[type].append(row[1:])
      else:
        iocs[type] = []
        iocs[type].append(row[1:])

  if iocs.get('dns'):
    x = 0
  if iocs.get('file_hash'):
    x = 0
  if iocs.get('file_path'):
    print("Checking File Paths...")
    for r in iocs['file_path']:
      print("-- {} :: ".format(r[0].strip()), end='')
      val = files.file_path(r[0].strip())
      print(val)
      
main(sys.argv[1])
