create or replace FUNCTION get_vendors_for_part(p_part_id integer)
returns table(vendor_id integer, vendor_name varchar)
LANGUAGE plpgsql
as $$
BEGIN
    select vendor_id, vendor_name
    from vendors v
    join part_vendors vp on vp.vendor_id = v.vendor_id
    where vp.part_id = p_part_id
END;
$$;