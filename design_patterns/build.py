class Car:
    def __init__(self):
        self.body = None
        self.color = None
        self.shade = None
        self.metallic = None

    def with_body(self, body):
        self.body = body
        return self

    def with_color(self, color, shade, metallic):
        self.color = color
        self.shade = shade
        self.metallic = metallic
        return self


audi = Car().with_color('alb', '2', True).with_body('sedan')