import sys
import os

from scrapy.cmdline import execute


cur_dir_name = os.path.dirname(os.path.abspath(__file__))
print("current directory name = %s" % cur_dir_name)
sys.path.append(cur_dir_name)

# execute(["scrapy", "crawl", "leetcode"])
execute(["scrapy", "crawl", "acwing"])

