# coding: utf-8

import imp


def loadPlugins(target, filters):
    pass


def splitPages(path, totalPage, curPage):
    result = []
    if totalPage <= 7:
        for num in range(1, totalPage + 1):
            result.append({
                'text': num,
                'url': path + '?page=' + str(num),
                'current': True if curPage == num else False
            })
        if len(result) != 1:
            if not result[0]['current']:
                result[0]['text'] = '首页'
            if not result[-1]['current']:
                result[-1]['text'] = '末页'
        return result
    maxPage = curPage + 3
    minPage = curPage - 3
    if curPage + 3 > totalPage:
        maxPage = totalPage
    if curPage - 3 <= 1:
        minPage = 1
    for num in range(minPage, maxPage + 1):
        result.append({
            'text': num,
            'url': path + '?page=' + str(num),
            'current': True if curPage == num else False
        })
    if not result[0]['current']:
        result.insert(0, {
            'text': '首页',
            'url': path + '?page=1',
            'current': False
        })
        result.insert(0, {
            'text': '上一页',
            'url': path + '?page=' + str(curPage - 1),
            'current': False
        })
    if not result[-1]['current']:
        result.append({
            'text': '末页',
            'url': path + '?page=' + str(totalPage),
            'current': False
        })
        result.append({
            'text': '下一页',
            'url': path + '?page=' + str(curPage + 1),
            'current': False
        })
    return result
