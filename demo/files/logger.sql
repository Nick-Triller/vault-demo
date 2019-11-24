CREATE ROLE "{{name}}" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}';
GRANT INSERT ON ALL TABLES IN SCHEMA public TO "{{name}}";
GRANT USAGE, SELECT ON SEQUENCE record_id_seq TO "{{name}}";
