class Language():

    def to_short(self,long_name):
        long_name = long_name.lower()
        if long_name == "czech":
            return "cs"
        if long_name == "english":
            return "en"

        return long_name

    def to_long(self,short_name):
        short_name = short_name.lower()
        if short_name == "cs":
            return "Czech"
        if short_name == "en":
            return "English"

        return short_name
