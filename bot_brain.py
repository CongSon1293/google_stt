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
    elif u'thích' in question and u'môn thể thao' in question:
        return u'Tôi thích bóng đá.'
    elif u'câu lạc bộ' in question:
        return u'Tôi là phan của man chét tơ ui nai tứt.'
    elif u'thủ đô' in question and u'việt nam' in question:
        return u'Thủ đô của Việt Nam là thành phố Hà Nội.'
    elif u'thủ tướng' in question and u'việt nam' in question:
        return u'Đó là ông Nguyễn Xuân Phúc.'
    elif question == u'':
        return u'Xin lỗi, tôi không nghe thấy bạn nói gì.'
    else:
        return u'Xin lỗi, tôi không hiểu câu hỏi "%s" của bạn' % (question)