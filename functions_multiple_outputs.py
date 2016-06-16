def rectangle(w, h):
    area = w * h;
    perimeter = w + w + h + h;
    return area, perimeter

rect_area, rect_peri = rectangle(2, 3);

print rect_area, rect_peri  # print 6 10