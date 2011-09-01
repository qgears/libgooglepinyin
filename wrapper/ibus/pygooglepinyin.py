#!/usr/bin/python
# -*- coding: UTF-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
'''libgooglepinyin wrapper for python with multiprocessing

'''

import multiprocessing
import atexit
import time
import os
import sys


class _Dummy(list):
    def __getattr__(*args):
        return lambda *args: None

_parent_conn, _child_conn, _im_open_decoder_args, _process = [_Dummy()] * 4

_exit = 0

def _on_exit():
    global _process
    global _exit
    _exit = 1
    _call("im_flush_cache")
    _process.terminate()
    return

def _launch_decoder(*args):
    global _parent_conn, _child_conn, _im_open_decoder_args, _process
    _parent_conn, _child_conn = multiprocessing.Pipe()
    if args:
        _im_open_decoder_args = args
        pass
    def process():
        import googlepinyin
        _child_conn.send(googlepinyin.im_open_decoder(*_im_open_decoder_args))
        def im_get_all_candidates(start, stop):
            candidates = []
            for i in range(start, stop):
                candidates.append(googlepinyin.im_get_candidate(i))
                pass
            return candidates
        googlepinyin.im_get_all_candidates = im_get_all_candidates
        while True:
            funcname, args, kwds = _child_conn.recv()
            func = googlepinyin.__dict__.get(funcname)
            if func:
                _child_conn.send(func(*args, **kwds))
                pass
            else:
                _child_conn.send(None)
                pass
            pass
        pass
    _process = multiprocessing.Process(target = process)
    _process.start()
    print _process.pid
    time.sleep(0.1)
    if (_on_exit, (), {}) not in atexit._exithandlers:
        atexit.register(_on_exit)
        pass
    pass

def _call(funcname, *args, **kwds):
    global _parent_conn, _child_conn, _im_open_decoder_args, _process
    global _exit
    _parent_conn.send((funcname, args, kwds))
    time.sleep(0.0001)
    for i in range(200):
        if _exit:
            time.sleep(0.1)
            return None
        if not _process.is_alive():
            _launch_decoder()
            _parent_conn.recv()
            return None
        if _parent_conn.poll():
            return _parent_conn.recv()
        time.sleep(0.0002)
        pass
    return None

def im_open_decoder(*args):
    _launch_decoder(*args)
    return _parent_conn.recv()

def im_close_decoder(*args, **kwds):
    return _call("im_close_decoder", *args, **kwds)

def im_set_max_lens(*args, **kwds):
    return _call("im_set_max_lens", *args, **kwds)

def im_flush_cache(*args, **kwds):
    return _call("im_flush_cache", *args, **kwds)

_num = 0

def im_search(*args, **kwds):
    global _num
    _num = _call("im_search", *args, **kwds)
    return _num

def im_delsearch(*args, **kwds):
    return _call("im_delsearch", *args, **kwds)

def im_reset_search(*args, **kwds):
    return _call("im_reset_search", *args, **kwds)

def im_get_sps_str(*args, **kwds):
    return _call("im_get_sps_str", *args, **kwds)

def im_get_candidate(*args, **kwds):
    return _call("im_get_candidate", *args, **kwds)

def im_get_all_candidates(start = 0, stop = 1000):
    global _num
    return _call("im_get_all_candidates", start, min(stop, _num))

def im_get_spl_start_pos(*args, **kwds):
    return _call("im_get_spl_start_pos", *args, **kwds)

def im_choose(*args, **kwds):
    global _num
    _num = _call("im_choose", *args, **kwds)
    return _num

def im_cancel_last_choice(*args, **kwds):
    return _call("im_cancel_last_choice", *args, **kwds)

def im_get_fixed_len(*args, **kwds):
    return _call("im_get_fixed_len", *args, **kwds)

def im_get_predicts(*args, **kwds):
    return _call("im_get_predicts", *args, **kwds)

def im_enable_shm_as_szm(*args, **kwds):
    return _call("im_enable_shm_as_szm", *args, **kwds)

def im_enable_ym_as_szm(*args, **kwds):
    return _call("im_enable_ym_as_szm", *args, **kwds)


if __name__=="__main__":
    if sys.argv[1:] and sys.argv[1].isalpha():
        pinyin = sys.argv[1]
        im_open_decoder()
        num = im_search(pinyin)
        #print '\t'.join(im_get_all_candidates())
        print '\t'.join((('%3s %s') % (i, im_get_candidate(i)) for i in range(num)))
        pass
    else:
        try:
            import readline
        except:
            pass
        im_open_decoder()
        num = 0
        while True:
            try:
                i = raw_input('> ')
            except:
                im_close_decoder()
                break
            if i and i[0].isalpha():
                im_reset_search()
                num = im_search(i)
                if num is None:
                    continue
                print '\t'.join((('%3s %s') % (i, im_get_candidate(i)) for i in range(num)))
                pass
            elif i.isdigit() and int(i) < num:
                num = im_choose(int(i))
                if num is None:
                    continue
                print '-', im_get_fixed_len()
                print '\t'.join((('%3s %s') % (i, im_get_candidate(i)) for i in range(num)))
                pass
            pass
        pass
    pass

