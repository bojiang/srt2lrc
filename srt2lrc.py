'''
Run it in srt file folder.
python 3.x
'''
import glob


def srt2lrc(num, time_str, content):
    ts, te = time_str.replace('\n','').split(' --> ')
    ts = ts[3:-1].replace(',','.')
    te = te[3:-1].replace(',','.')
    co = content.replace('\n', ' ')
    return '[%s]%s\n[%s]\n' % (ts, co, te)


if __name__ == '__main__':
    for fname in glob.glob('*.srt'):
        with open(fname, encoding='utf8') as f:
            fs = f.read()
            out = ''.join([srt2lrc(*line.split('\n', 2)) for line in fs.replace('\r\n', '\n').split('\n\n')])
            with open(fname.replace('srt', 'lrc'), 'w', encoding='utf8') as of:
                of.write(out)
