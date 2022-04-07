from flask_app.config.mysqlconnection import connectToMySQL

db_name = 'token_records'

class Nft:
    def __init__( self , data ):
        self.id = data['id']
        self.status = data['status']
        self.image_name = data['image_name']
        self.collection_name = data['collection_name']
        self.token_number = data['token_number']
        self.collection_link_to_exchange = data['collection_link_to_exchange']
        self.purchase_price = data['purchase_price']
        self.date_of_purchase = data['date_of_purchase']
        self.date_of_sale = data['date_of_sale']
        self.trade_fees = data['trade_fees']
        self.has_staking = data['has_staking']
        self.notes = data['notes']
        self.is_for_sale = data['is_for_sale']
        self.sale_price = data['sale_price']
        self.link_to_sale = data['link_to_sale']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO nfts ( image_name , status , collection_name , token_number , collection_link_to_exchange , purchase_price,  date_of_purchase , date_of_sale , trade_fees , has_staking , notes , is_for_sale , sale_price , link_to_sale , user_id) VALUES (%(image_name)s, %(status)s, %(collection_name)s, %(token_number)s, %(collection_link_to_exchange)s, %(purchase_price)s, %(date_of_purchase)s, %(date_of_sale)s, %(trade_fees)s, %(has_staking)s, %(notes)s, %(is_for_sale)s, %(sale_price)s, %(link_to_sale)s, %(user_id)s)"
        return connectToMySQL(db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM nfts JOIN users ON users.id = nfts.user_id;"
        results = connectToMySQL(db_name).query_db(query)
        collections = []
        for collection in results:
            collections.append( cls(collection) )
        # favorites.sort(reverse=True)
        return collections

    # @classmethod
    # def get_by_id(cls, data):
    #     query = "SELECT * FROM nfts WHERE id = %(id)s";
    #     result = connectToMySQL(db_name).query_db(query, data)
    #     return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM nfts JOIN users ON users.id = nfts.user_id WHERE nfts.id = %(id)s";
        result = connectToMySQL(db_name).query_db(query, data)
        return cls(result[0])

    # @classmethod
    # def get_image_name(cls, data):
    #     query = "SELECT image_name FROM nfts JOIN users ON users.id = nfts.user_id WHERE nfts.id = %(id)s";
    #     result = connectToMySQL(db_name).query_db(query, data)
    #     return cls(result[0])

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM nfts WHERE id = %(id)s;"
        return connectToMySQL(db_name).query_db(query,data)

    @classmethod
    def update(cls, data):
        query = "UPDATE nfts JOIN users ON users.id = nfts.user_id SET status=%(status)s, image_name=%(image_name)s, collection_name=%(collection_name)s, token_number=%(token_number)s, collection_link_to_exchange=%(collection_link_to_exchange)s, purchase_price=%(purchase_price)s, date_of_purchase=%(date_of_purchase)s, date_of_sale=%(date_of_sale)s, trade_fees=%(trade_fees)s, has_staking=%(has_staking)s, notes=%(notes)s, is_for_sale=%(is_for_sale)s, sale_price=%(sale_price)s, link_to_sale=%(link_to_sale)s WHERE nfts.id = %(nft_id)s;"
        return connectToMySQL(db_name).query_db(query, data)

    # @staticmethod
    # def validate_new_user(x):
    #     is_valid = True
    #     query = "SELECT * FROM users WHERE email = %(email)s;"
    #     results = connectToMySQL(db_name).query_db(query, x)
    #     if len(results) >= 1:
    #         flash("Email already taken." , "register")
    #         is_valid=False
    #     if not EMAIL_REGEX.match(x['email']):
    #         flash("Invalid email address." , "register")
    #         is_valid=False
    #     if len(x['first_name']) < 2:
    #         flash("First name must be at least 2 characters." , "register")
    #         is_valid=False
    #     if len(x['last_name']) < 2:
    #         flash("Last name must be at least 2 characters." , "register")
    #         is_valid = False
    #     if len(x['password']) < 8:
    #         flash("Password must be at least 8 characters." , "register")
    #         is_valid = False
    #     if x['password'] != x['confirm_password']:
    #         flash("Passwords do not match!" , "register")
    #         is_valid = False
    #     return is_valid