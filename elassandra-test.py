from cassandra.cqlengine.models import Model
from cassandra.cqlengine.columns import Text, DateTime
from cassandra.cqlengine import connection
from cassandra.cqlengine import management
from cassandra.policies import DCAwareRoundRobinPolicy

class Product(Model):
    code = Text(primary_key=True)
    url = Text()
    created_t = DateTime()
    product_name = Text()


keyspace="app"
connection.setup(["127.0.0.1"], default_keyspace=keyspace, protocol_version=3,
                     load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='DC1'),
                     retry_connect=True)

management.create_keyspace_network_topology(keyspace, {'DC1': 1})
management.sync_table(Product, keyspaces=[keyspace]