-- Delete old procedures/functions if they already exist.
-- This helps us run this file many times without conflict.
drop procedure if exists add_phone(varchar, varchar, varchar);
drop procedure if exists move_to_group(varchar, varchar);
drop function if exists search_contacts(varchar);
drop function if exists get_contacts_page(int, int);


-- Procedure to add phone number to existing contact.
create or replace procedure add_phone(
    p_name varchar,
    p_phone varchar,
    p_type varchar
)
language plpgsql
as $$
declare
    -- Temporary variable for contact id.
    cid int;
begin
    -- Find contact id by name.
    select id into cid
    from contacts
    where lower(name) = lower(p_name);

    -- If contact exists, add phone number.
    if cid is not null then
        insert into phones(contact_id, phone, phone_type)
        values (cid, p_phone, p_type);
    else
        raise notice 'Contact not found';
    end if;
end;
$$;


-- Procedure to move contact to another group.
-- If group does not exist, it creates a new group.
create or replace procedure move_to_group(
    p_name varchar,
    p_group varchar
)
language plpgsql
as $$
declare
    -- Temporary variable for group id.
    gid int;
begin
    -- Try to find group by name.
    select id into gid
    from groups
    where lower(name) = lower(p_group);

    -- If group does not exist, create it.
    if gid is null then
        insert into groups(name)
        values (p_group)
        returning id into gid;
    end if;

    -- Update contact group.
    update contacts
    set group_id = gid
    where lower(name) = lower(p_name);
end;
$$;


-- Function to search contacts by name, email, phone, or group.
create or replace function search_contacts(p_query varchar)
returns table(
    name varchar,
    email varchar,
    birthday date,
    group_name varchar,
    phone varchar,
    phone_type varchar,
    created_at timestamp
)
language plpgsql
as $$
begin
    return query
    select
        c.name,
        c.email,
        c.birthday,
        g.name,
        p.phone,
        p.phone_type,
        c.created_at
    from contacts c
    left join groups g on c.group_id = g.id
    left join phones p on c.id = p.contact_id
    where
        c.name ilike '%' || p_query || '%'
        or c.email ilike '%' || p_query || '%'
        or p.phone ilike '%' || p_query || '%'
        or g.name ilike '%' || p_query || '%';
end;
$$;


-- Function for pagination.
-- p_limit means how many rows per page.
-- p_offset means how many rows to skip.
create or replace function get_contacts_page(
    p_limit int,
    p_offset int
)
returns table(
    name varchar,
    email varchar,
    birthday date,
    group_name varchar,
    phone varchar
)
language plpgsql
as $$
begin
    return query
    select
        c.name,
        c.email,
        c.birthday,
        g.name,
        p.phone
    from contacts c
    left join groups g on c.group_id = g.id
    left join phones p on c.id = p.contact_id
    order by c.id
    limit p_limit offset p_offset;
end;
$$;