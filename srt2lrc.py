'''
Run it in srt file folder.
python 3.x
'''
import glob


def srt_block_to_irc(block):
    infos = block.split('\n', 2)
    if not infos or not len(infos) == 3:
        return None
    num, time_str, content = infos
    ts, te = time_str.replace('\n', '').split(' --> ')
    ts = ts[3:-1].replace(',', '.')
    te = te[3:-1].replace(',', '.')
    co = content.replace('\n', ' ')
    return '[%s]%s\n[%s]\n' % (ts, co, te)


def srt_file_to_irc(fname):
    with open(fname, encoding='utf8') as file_in:
        str_in = file_in.read()
        blocks_in = str_in.replace('\r\n', '\n').split('\n\n')
        blocks_out = [srt_block_to_irc(block) for block in blocks_in]
        if not all(blocks_out):
            err_info.append((fname, blocks_out.index(None), blocks_in[blocks_out.index(None)]))
        blocks_out = filter(None, blocks_out)
        str_out = ''.join(blocks_out)
        with open(fname.replace('srt', 'lrc'), 'w', encoding='utf8') as file_out:
            file_out.write(str_out)


if __name__ == '__main__':
    err_info = []
    for file_name in glob.glob('*.srt'):
        srt_file_to_irc(file_name)
    if err_info:
        print('success, but some exceptions are ignored:')
        for file_name, blocks_num, context in err_info:
            print('\tfile: %s, block num: %s, context: %s' % (file_name, blocks_num, context))
    else:
        print('success')
