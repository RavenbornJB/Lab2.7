from time import time, sleep
import cache_webpage


if __name__ == '__main__':
    my_file = "https://gist.githubusercontent.com/RavenbornJB/53a2b38712" \
              "f5dccdca18f2b297aee7b5/raw/0824d6f6890cd0735334176224e3bfcc863ae28e/testrr.txt"
    webpage = cache_webpage.WebPage(my_file)
    now = time()
    content1 = webpage.content
    t1 = time() - now
    print(t1)
    now = time()
    content2 = webpage.content
    t2 = time() - now
    print(t2)
    assert t2 < t1
    assert content1 == content2
    sleep(11)
    now = time()
    content3 = webpage.content
    assert content3 == b'Andriy Romanyuk, Oles Dobosevych'
    t3 = time() - now
