PGDMP     ;                	    {         
   db_refugio    11.21    11.21     �
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �
           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �
           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            �
           1262    16873 
   db_refugio    DATABASE     �   CREATE DATABASE db_refugio WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Spain.1252' LC_CTYPE = 'Spanish_Spain.1252';
    DROP DATABASE db_refugio;
             postgres    false            �            1259    16874    empleado    TABLE     �   CREATE TABLE public.empleado (
    "DNI" integer NOT NULL,
    "Apellido" character varying(50),
    "Nombre" character varying(50),
    "Fecha de Ingreso" date
);
    DROP TABLE public.empleado;
       public         postgres    false            �
          0    16874    empleado 
   TABLE DATA               S   COPY public.empleado ("DNI", "Apellido", "Nombre", "Fecha de Ingreso") FROM stdin;
    public       postgres    false    196   �       |
           2606    16878    empleado pk_empleado 
   CONSTRAINT     U   ALTER TABLE ONLY public.empleado
    ADD CONSTRAINT pk_empleado PRIMARY KEY ("DNI");
 >   ALTER TABLE ONLY public.empleado DROP CONSTRAINT pk_empleado;
       public         postgres    false    196            �
   �   x�E�=n�0�g�.*DZ�c���Rnѩ��x�J�l/�M�9�/Vv
\���h��쨁�0\��c.�0`ɍ�u4�lC��[���P⮳��d���y��wHS/���z7�dёWF��K(�zO5�R��d;lX{��{.�ᐮe���(A�UgiHå��m��G�`Fj���*8紬��&��L���Z55����a*�{����d�ch�8��՗i�u}*m�7p�[J�����'D�&�\x     