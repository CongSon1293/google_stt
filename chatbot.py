# -*- encoding: utf-8 -*-

def get_response(question):
    question = question.lower()
    if u'tên' in question:
        return u'Tên tôi là Nobita.'
    elif u'tuổi' in question:
        return u'Tôi được 1 ngày tuổi.'
    elif u'ai' in question and u'tạo ra' in question:
        return u'Là một thằng nhóc thích truyện đô rê mon'
    elif u'thời tiết' in question and u'hôm nay' in question:
        return u'Nhìn ra ngoài là biết, sao phải hỏi.'
    elif u'thời tiết' in question and u'hôm qua' in question:
        return u'Tối qua mưa to.'
    elif u'thời tiết' in question:
        return u'Sáng nắng, chiều mưa, giữa trưa có bão.'
    elif u'hôm nay' in question and u'thứ mấy' in question:
        return u'Tra lịch để biết câu trả lời nhé.'
    else:
        return u'Xin lỗi, tôi không hiểu câu hỏi "%s" của bạn' % (question)