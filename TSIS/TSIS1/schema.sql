-- Delete old tables if they already exist.
-- We delete phones first because phones depends on contacts.
-- Contacts depends on groups, so groups should be deleted last.
drop table if exists phones cascade;
drop table if exists contacts cascade;
drop table if exists groups cascade;


-- This table stores contact categories:
-- Family, Friends, Work, University, etc.
create table groups (
    id serial primary key,
    name varchar(100) unique not null
);


-- This table stores main contact information.
-- name is unique because in this project we use name to find contact.
create table contacts (
    id serial primary key,
    name varchar(100) unique not null,
    email varchar(150),
    birthday date,
    group_id int references groups(id) on delete set null,
    created_at timestamp default current_timestamp
);


-- This table stores phone numbers.
-- One contact can have many phone numbers.
create table phones (
    id serial primary key,
    contact_id int references contacts(id) on delete cascade,
    phone varchar(30) not null,
    phone_type varchar(30) default 'mobile'
);


-- Add default groups.
-- on conflict do nothing prevents error if group already exists.
insert into groups(name)
values 
    ('Family'), 
    ('Friends'), 
    ('Work')
on conflict (name) do nothing;