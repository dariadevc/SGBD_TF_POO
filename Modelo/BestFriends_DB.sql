PGDMP  2                
    {            BestFriends_DB    16.0    16.0 X               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16455    BestFriends_DB    DATABASE     �   CREATE DATABASE "BestFriends_DB" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Argentina.1252';
     DROP DATABASE "BestFriends_DB";
                postgres    false            �            1259    16626    adopcion    TABLE     �   CREATE TABLE public.adopcion (
    id_adopcion integer NOT NULL,
    id_usuario integer NOT NULL,
    id_adoptante integer NOT NULL,
    id_animal integer NOT NULL,
    fecha_adopcion date NOT NULL
);
    DROP TABLE public.adopcion;
       public         heap    postgres    false            �            1259    16625    ADOPCION_id_adopcion_seq    SEQUENCE     �   CREATE SEQUENCE public."ADOPCION_id_adopcion_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public."ADOPCION_id_adopcion_seq";
       public          postgres    false    236                       0    0    ADOPCION_id_adopcion_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public."ADOPCION_id_adopcion_seq" OWNED BY public.adopcion.id_adopcion;
          public          postgres    false    235            �            1259    16521    adoptante_visitante    TABLE     �  CREATE TABLE public.adoptante_visitante (
    id_adoptante_visitante integer NOT NULL,
    nombre_adoptante_visitante character varying(20) NOT NULL,
    apellido_adoptante_visitante character varying(20) NOT NULL,
    dni_adoptante_visitante integer NOT NULL,
    nro_cel_adoptante_visitante character varying(10) NOT NULL,
    email_adoptante_visitante character varying(30) NOT NULL,
    direccion_adoptante character varying(40),
    fecha_registro_adoptante date,
    condicion_adoptante_visitante character varying(10) NOT NULL,
    adoptante_visitante_eliminado boolean DEFAULT false NOT NULL,
    causa_baja_adoptante_visitante character varying(250)
);
 '   DROP TABLE public.adoptante_visitante;
       public         heap    postgres    false            �            1259    16520 .   ADOPTANTE_VISITANTE_id_adoptante_visitante_seq    SEQUENCE     �   CREATE SEQUENCE public."ADOPTANTE_VISITANTE_id_adoptante_visitante_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 G   DROP SEQUENCE public."ADOPTANTE_VISITANTE_id_adoptante_visitante_seq";
       public          postgres    false    224                       0    0 .   ADOPTANTE_VISITANTE_id_adoptante_visitante_seq    SEQUENCE OWNED BY     �   ALTER SEQUENCE public."ADOPTANTE_VISITANTE_id_adoptante_visitante_seq" OWNED BY public.adoptante_visitante.id_adoptante_visitante;
          public          postgres    false    223            �            1259    16503    animal    TABLE     �  CREATE TABLE public.animal (
    id_animal integer NOT NULL,
    codigo_animal character varying(10) NOT NULL,
    tipo_animal character varying(10) NOT NULL,
    nombre_animal character varying(20) NOT NULL,
    sexo_animal character varying(10) NOT NULL,
    etapa_vida_animal character varying(10) NOT NULL,
    edad_estimada_animal integer NOT NULL,
    peso_animal numeric(3,2),
    "tamaño_animal" character varying(20) NOT NULL,
    descripcion_animal character varying(250),
    animal_castrado boolean NOT NULL,
    fecha_nacimiento_estimada_animal date,
    ingreso_refugio_animal date NOT NULL,
    animal_eliminado boolean DEFAULT false NOT NULL,
    causa_baja_animal character varying(250)
);
    DROP TABLE public.animal;
       public         heap    postgres    false            �            1259    16502    ANIMAL_id_animal_seq    SEQUENCE     �   CREATE SEQUENCE public."ANIMAL_id_animal_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public."ANIMAL_id_animal_seq";
       public          postgres    false    220                       0    0    ANIMAL_id_animal_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public."ANIMAL_id_animal_seq" OWNED BY public.animal.id_animal;
          public          postgres    false    219            �            1259    16619    horario_visita    TABLE     �   CREATE TABLE public.horario_visita (
    id_horario_visita integer NOT NULL,
    inicio_horario_visita character varying(5) NOT NULL,
    fin_horario_visita character varying(5) NOT NULL
);
 "   DROP TABLE public.horario_visita;
       public         heap    postgres    false            �            1259    16618 #   HORARIO_VISTA_id_horario_visita_seq    SEQUENCE     �   CREATE SEQUENCE public."HORARIO_VISTA_id_horario_visita_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 <   DROP SEQUENCE public."HORARIO_VISTA_id_horario_visita_seq";
       public          postgres    false    234                       0    0 #   HORARIO_VISTA_id_horario_visita_seq    SEQUENCE OWNED BY     n   ALTER SEQUENCE public."HORARIO_VISTA_id_horario_visita_seq" OWNED BY public.horario_visita.id_horario_visita;
          public          postgres    false    233            �            1259    16469    registro_sesiones    TABLE     �   CREATE TABLE public.registro_sesiones (
    id_usuario integer NOT NULL,
    fecha_sesion timestamp without time zone DEFAULT now() NOT NULL
);
 %   DROP TABLE public.registro_sesiones;
       public         heap    postgres    false            �            1259    16468     REGISTRO_SESIONES_id_usuario_seq    SEQUENCE     �   CREATE SEQUENCE public."REGISTRO_SESIONES_id_usuario_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public."REGISTRO_SESIONES_id_usuario_seq";
       public          postgres    false    218                       0    0     REGISTRO_SESIONES_id_usuario_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public."REGISTRO_SESIONES_id_usuario_seq" OWNED BY public.registro_sesiones.id_usuario;
          public          postgres    false    217            �            1259    16462    usuario    TABLE     �  CREATE TABLE public.usuario (
    id_usuario integer NOT NULL,
    tipo_usuario character varying(10) NOT NULL,
    dni_usuario integer NOT NULL,
    apellido_usuario character varying(20) NOT NULL,
    nombre_usuario character varying(20) NOT NULL,
    alias_usuario integer NOT NULL,
    fecha_registro_usuario timestamp without time zone DEFAULT now() NOT NULL,
    nro_cel_usuario character varying(10) NOT NULL,
    email_usuario character varying(30) NOT NULL,
    contrasenia_usuario character varying(20) NOT NULL,
    cuil_usuario character varying(13) NOT NULL,
    permisos_adopcion boolean NOT NULL,
    usuario_eliminado boolean DEFAULT false NOT NULL,
    causa_baja_usuario character varying(250)
);
    DROP TABLE public.usuario;
       public         heap    postgres    false            �            1259    16461    USUARIO_id_usuario_seq    SEQUENCE     �   CREATE SEQUENCE public."USUARIO_id_usuario_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public."USUARIO_id_usuario_seq";
       public          postgres    false    216                       0    0    USUARIO_id_usuario_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public."USUARIO_id_usuario_seq" OWNED BY public.usuario.id_usuario;
          public          postgres    false    215            �            1259    16514    VACUNA    TABLE     �   CREATE TABLE public."VACUNA" (
    id_vacuna integer NOT NULL,
    nombre_vacuna character varying(20) NOT NULL,
    funcion_vacuna character varying(250) NOT NULL
);
    DROP TABLE public."VACUNA";
       public         heap    postgres    false            �            1259    16530    VACUNAS_APLCIADAS    TABLE     �   CREATE TABLE public."VACUNAS_APLCIADAS" (
    id_vacuna integer NOT NULL,
    id_animal integer NOT NULL,
    fecha_aplicacion date NOT NULL,
    proxima_aplicacion date NOT NULL
);
 '   DROP TABLE public."VACUNAS_APLCIADAS";
       public         heap    postgres    false            �            1259    16529    VACUNAS_APLCIADAS_id_animal_seq    SEQUENCE     �   CREATE SEQUENCE public."VACUNAS_APLCIADAS_id_animal_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public."VACUNAS_APLCIADAS_id_animal_seq";
       public          postgres    false    227                        0    0    VACUNAS_APLCIADAS_id_animal_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public."VACUNAS_APLCIADAS_id_animal_seq" OWNED BY public."VACUNAS_APLCIADAS".id_animal;
          public          postgres    false    226            �            1259    16528    VACUNAS_APLCIADAS_id_vacuna_seq    SEQUENCE     �   CREATE SEQUENCE public."VACUNAS_APLCIADAS_id_vacuna_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public."VACUNAS_APLCIADAS_id_vacuna_seq";
       public          postgres    false    227            !           0    0    VACUNAS_APLCIADAS_id_vacuna_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public."VACUNAS_APLCIADAS_id_vacuna_seq" OWNED BY public."VACUNAS_APLCIADAS".id_vacuna;
          public          postgres    false    225            �            1259    16513    VACUNA_id_vacuna_seq    SEQUENCE     �   CREATE SEQUENCE public."VACUNA_id_vacuna_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public."VACUNA_id_vacuna_seq";
       public          postgres    false    222            "           0    0    VACUNA_id_vacuna_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public."VACUNA_id_vacuna_seq" OWNED BY public."VACUNA".id_vacuna;
          public          postgres    false    221            �            1259    16580    visita_juego    TABLE     ?  CREATE TABLE public.visita_juego (
    id_visita_juego integer NOT NULL,
    id_usuario integer NOT NULL,
    id_visitante integer NOT NULL,
    id_animal integer NOT NULL,
    fecha_visita_juego date NOT NULL,
    id_hora_visita character varying(5) NOT NULL,
    estado_visita_juego character varying(10) NOT NULL
);
     DROP TABLE public.visita_juego;
       public         heap    postgres    false            �            1259    16579    VISITA_JUEGO_id_animal_seq    SEQUENCE     �   CREATE SEQUENCE public."VISITA_JUEGO_id_animal_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public."VISITA_JUEGO_id_animal_seq";
       public          postgres    false    232            #           0    0    VISITA_JUEGO_id_animal_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public."VISITA_JUEGO_id_animal_seq" OWNED BY public.visita_juego.id_animal;
          public          postgres    false    231            �            1259    16577    VISITA_JUEGO_id_usuario_seq    SEQUENCE     �   CREATE SEQUENCE public."VISITA_JUEGO_id_usuario_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public."VISITA_JUEGO_id_usuario_seq";
       public          postgres    false    232            $           0    0    VISITA_JUEGO_id_usuario_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public."VISITA_JUEGO_id_usuario_seq" OWNED BY public.visita_juego.id_usuario;
          public          postgres    false    229            �            1259    16576     VISITA_JUEGO_id_visita_juego_seq    SEQUENCE     �   CREATE SEQUENCE public."VISITA_JUEGO_id_visita_juego_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public."VISITA_JUEGO_id_visita_juego_seq";
       public          postgres    false    232            %           0    0     VISITA_JUEGO_id_visita_juego_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public."VISITA_JUEGO_id_visita_juego_seq" OWNED BY public.visita_juego.id_visita_juego;
          public          postgres    false    228            �            1259    16578    VISITA_JUEGO_id_visitante_seq    SEQUENCE     �   CREATE SEQUENCE public."VISITA_JUEGO_id_visitante_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public."VISITA_JUEGO_id_visitante_seq";
       public          postgres    false    232            &           0    0    VISITA_JUEGO_id_visitante_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public."VISITA_JUEGO_id_visitante_seq" OWNED BY public.visita_juego.id_visitante;
          public          postgres    false    230            L           2604    16517    VACUNA id_vacuna    DEFAULT     x   ALTER TABLE ONLY public."VACUNA" ALTER COLUMN id_vacuna SET DEFAULT nextval('public."VACUNA_id_vacuna_seq"'::regclass);
 A   ALTER TABLE public."VACUNA" ALTER COLUMN id_vacuna DROP DEFAULT;
       public          postgres    false    222    221    222            O           2604    16533    VACUNAS_APLCIADAS id_vacuna    DEFAULT     �   ALTER TABLE ONLY public."VACUNAS_APLCIADAS" ALTER COLUMN id_vacuna SET DEFAULT nextval('public."VACUNAS_APLCIADAS_id_vacuna_seq"'::regclass);
 L   ALTER TABLE public."VACUNAS_APLCIADAS" ALTER COLUMN id_vacuna DROP DEFAULT;
       public          postgres    false    227    225    227            P           2604    16534    VACUNAS_APLCIADAS id_animal    DEFAULT     �   ALTER TABLE ONLY public."VACUNAS_APLCIADAS" ALTER COLUMN id_animal SET DEFAULT nextval('public."VACUNAS_APLCIADAS_id_animal_seq"'::regclass);
 L   ALTER TABLE public."VACUNAS_APLCIADAS" ALTER COLUMN id_animal DROP DEFAULT;
       public          postgres    false    227    226    227            S           2604    16629    adopcion id_adopcion    DEFAULT     ~   ALTER TABLE ONLY public.adopcion ALTER COLUMN id_adopcion SET DEFAULT nextval('public."ADOPCION_id_adopcion_seq"'::regclass);
 C   ALTER TABLE public.adopcion ALTER COLUMN id_adopcion DROP DEFAULT;
       public          postgres    false    236    235    236            M           2604    16524 *   adoptante_visitante id_adoptante_visitante    DEFAULT     �   ALTER TABLE ONLY public.adoptante_visitante ALTER COLUMN id_adoptante_visitante SET DEFAULT nextval('public."ADOPTANTE_VISITANTE_id_adoptante_visitante_seq"'::regclass);
 Y   ALTER TABLE public.adoptante_visitante ALTER COLUMN id_adoptante_visitante DROP DEFAULT;
       public          postgres    false    223    224    224            J           2604    16506    animal id_animal    DEFAULT     v   ALTER TABLE ONLY public.animal ALTER COLUMN id_animal SET DEFAULT nextval('public."ANIMAL_id_animal_seq"'::regclass);
 ?   ALTER TABLE public.animal ALTER COLUMN id_animal DROP DEFAULT;
       public          postgres    false    220    219    220            R           2604    16622     horario_visita id_horario_visita    DEFAULT     �   ALTER TABLE ONLY public.horario_visita ALTER COLUMN id_horario_visita SET DEFAULT nextval('public."HORARIO_VISTA_id_horario_visita_seq"'::regclass);
 O   ALTER TABLE public.horario_visita ALTER COLUMN id_horario_visita DROP DEFAULT;
       public          postgres    false    233    234    234            F           2604    16465    usuario id_usuario    DEFAULT     z   ALTER TABLE ONLY public.usuario ALTER COLUMN id_usuario SET DEFAULT nextval('public."USUARIO_id_usuario_seq"'::regclass);
 A   ALTER TABLE public.usuario ALTER COLUMN id_usuario DROP DEFAULT;
       public          postgres    false    215    216    216            Q           2604    16583    visita_juego id_visita_juego    DEFAULT     �   ALTER TABLE ONLY public.visita_juego ALTER COLUMN id_visita_juego SET DEFAULT nextval('public."VISITA_JUEGO_id_visita_juego_seq"'::regclass);
 K   ALTER TABLE public.visita_juego ALTER COLUMN id_visita_juego DROP DEFAULT;
       public          postgres    false    232    228    232                      0    16514    VACUNA 
   TABLE DATA           L   COPY public."VACUNA" (id_vacuna, nombre_vacuna, funcion_vacuna) FROM stdin;
    public          postgres    false    222   Gu       
          0    16530    VACUNAS_APLCIADAS 
   TABLE DATA           i   COPY public."VACUNAS_APLCIADAS" (id_vacuna, id_animal, fecha_aplicacion, proxima_aplicacion) FROM stdin;
    public          postgres    false    227   du                 0    16626    adopcion 
   TABLE DATA           d   COPY public.adopcion (id_adopcion, id_usuario, id_adoptante, id_animal, fecha_adopcion) FROM stdin;
    public          postgres    false    236   �u                 0    16521    adoptante_visitante 
   TABLE DATA           ]  COPY public.adoptante_visitante (id_adoptante_visitante, nombre_adoptante_visitante, apellido_adoptante_visitante, dni_adoptante_visitante, nro_cel_adoptante_visitante, email_adoptante_visitante, direccion_adoptante, fecha_registro_adoptante, condicion_adoptante_visitante, adoptante_visitante_eliminado, causa_baja_adoptante_visitante) FROM stdin;
    public          postgres    false    224   �u                 0    16503    animal 
   TABLE DATA           /  COPY public.animal (id_animal, codigo_animal, tipo_animal, nombre_animal, sexo_animal, etapa_vida_animal, edad_estimada_animal, peso_animal, "tamaño_animal", descripcion_animal, animal_castrado, fecha_nacimiento_estimada_animal, ingreso_refugio_animal, animal_eliminado, causa_baja_animal) FROM stdin;
    public          postgres    false    220   �u                 0    16619    horario_visita 
   TABLE DATA           f   COPY public.horario_visita (id_horario_visita, inicio_horario_visita, fin_horario_visita) FROM stdin;
    public          postgres    false    234   6v                 0    16469    registro_sesiones 
   TABLE DATA           E   COPY public.registro_sesiones (id_usuario, fecha_sesion) FROM stdin;
    public          postgres    false    218   �v       �          0    16462    usuario 
   TABLE DATA             COPY public.usuario (id_usuario, tipo_usuario, dni_usuario, apellido_usuario, nombre_usuario, alias_usuario, fecha_registro_usuario, nro_cel_usuario, email_usuario, contrasenia_usuario, cuil_usuario, permisos_adopcion, usuario_eliminado, causa_baja_usuario) FROM stdin;
    public          postgres    false    216   �v                 0    16580    visita_juego 
   TABLE DATA           �   COPY public.visita_juego (id_visita_juego, id_usuario, id_visitante, id_animal, fecha_visita_juego, id_hora_visita, estado_visita_juego) FROM stdin;
    public          postgres    false    232   x       '           0    0    ADOPCION_id_adopcion_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public."ADOPCION_id_adopcion_seq"', 1, false);
          public          postgres    false    235            (           0    0 .   ADOPTANTE_VISITANTE_id_adoptante_visitante_seq    SEQUENCE SET     _   SELECT pg_catalog.setval('public."ADOPTANTE_VISITANTE_id_adoptante_visitante_seq"', 1, false);
          public          postgres    false    223            )           0    0    ANIMAL_id_animal_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public."ANIMAL_id_animal_seq"', 1, true);
          public          postgres    false    219            *           0    0 #   HORARIO_VISTA_id_horario_visita_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('public."HORARIO_VISTA_id_horario_visita_seq"', 4, true);
          public          postgres    false    233            +           0    0     REGISTRO_SESIONES_id_usuario_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public."REGISTRO_SESIONES_id_usuario_seq"', 1, true);
          public          postgres    false    217            ,           0    0    USUARIO_id_usuario_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public."USUARIO_id_usuario_seq"', 6, true);
          public          postgres    false    215            -           0    0    VACUNAS_APLCIADAS_id_animal_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public."VACUNAS_APLCIADAS_id_animal_seq"', 1, false);
          public          postgres    false    226            .           0    0    VACUNAS_APLCIADAS_id_vacuna_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public."VACUNAS_APLCIADAS_id_vacuna_seq"', 1, false);
          public          postgres    false    225            /           0    0    VACUNA_id_vacuna_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public."VACUNA_id_vacuna_seq"', 1, false);
          public          postgres    false    221            0           0    0    VISITA_JUEGO_id_animal_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public."VISITA_JUEGO_id_animal_seq"', 1, false);
          public          postgres    false    231            1           0    0    VISITA_JUEGO_id_usuario_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public."VISITA_JUEGO_id_usuario_seq"', 1, false);
          public          postgres    false    229            2           0    0     VISITA_JUEGO_id_visita_juego_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('public."VISITA_JUEGO_id_visita_juego_seq"', 1, false);
          public          postgres    false    228            3           0    0    VISITA_JUEGO_id_visitante_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public."VISITA_JUEGO_id_visitante_seq"', 1, false);
          public          postgres    false    230            e           2606    16631    adopcion ADOPCION_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.adopcion
    ADD CONSTRAINT "ADOPCION_pkey" PRIMARY KEY (id_adopcion);
 B   ALTER TABLE ONLY public.adopcion DROP CONSTRAINT "ADOPCION_pkey";
       public            postgres    false    236            ]           2606    16527 ,   adoptante_visitante ADOPTANTE_VISITANTE_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.adoptante_visitante
    ADD CONSTRAINT "ADOPTANTE_VISITANTE_pkey" PRIMARY KEY (id_adoptante_visitante);
 X   ALTER TABLE ONLY public.adoptante_visitante DROP CONSTRAINT "ADOPTANTE_VISITANTE_pkey";
       public            postgres    false    224            Y           2606    16508    animal ANIMAL_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.animal
    ADD CONSTRAINT "ANIMAL_pkey" PRIMARY KEY (id_animal);
 >   ALTER TABLE ONLY public.animal DROP CONSTRAINT "ANIMAL_pkey";
       public            postgres    false    220            c           2606    16624 !   horario_visita HORARIO_VISTA_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.horario_visita
    ADD CONSTRAINT "HORARIO_VISTA_pkey" PRIMARY KEY (id_horario_visita);
 M   ALTER TABLE ONLY public.horario_visita DROP CONSTRAINT "HORARIO_VISTA_pkey";
       public            postgres    false    234            W           2606    16496 (   registro_sesiones REGISTRO_SESIONES_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.registro_sesiones
    ADD CONSTRAINT "REGISTRO_SESIONES_pkey" PRIMARY KEY (id_usuario, fecha_sesion);
 T   ALTER TABLE ONLY public.registro_sesiones DROP CONSTRAINT "REGISTRO_SESIONES_pkey";
       public            postgres    false    218    218            U           2606    16467    usuario USUARIO_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT "USUARIO_pkey" PRIMARY KEY (id_usuario);
 @   ALTER TABLE ONLY public.usuario DROP CONSTRAINT "USUARIO_pkey";
       public            postgres    false    216            _           2606    16536 (   VACUNAS_APLCIADAS VACUNAS_APLCIADAS_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY public."VACUNAS_APLCIADAS"
    ADD CONSTRAINT "VACUNAS_APLCIADAS_pkey" PRIMARY KEY (id_vacuna, id_animal);
 V   ALTER TABLE ONLY public."VACUNAS_APLCIADAS" DROP CONSTRAINT "VACUNAS_APLCIADAS_pkey";
       public            postgres    false    227    227            [           2606    16519    VACUNA VACUNA_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public."VACUNA"
    ADD CONSTRAINT "VACUNA_pkey" PRIMARY KEY (id_vacuna);
 @   ALTER TABLE ONLY public."VACUNA" DROP CONSTRAINT "VACUNA_pkey";
       public            postgres    false    222            a           2606    16588    visita_juego VISITA_JUEGO_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.visita_juego
    ADD CONSTRAINT "VISITA_JUEGO_pkey" PRIMARY KEY (id_visita_juego);
 J   ALTER TABLE ONLY public.visita_juego DROP CONSTRAINT "VISITA_JUEGO_pkey";
       public            postgres    false    232            l           2606    16637 #   adopcion ADOPCION_id_adoptante_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.adopcion
    ADD CONSTRAINT "ADOPCION_id_adoptante_fkey" FOREIGN KEY (id_adoptante) REFERENCES public.adoptante_visitante(id_adoptante_visitante);
 O   ALTER TABLE ONLY public.adopcion DROP CONSTRAINT "ADOPCION_id_adoptante_fkey";
       public          postgres    false    4701    224    236            m           2606    16642     adopcion ADOPCION_id_animal_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.adopcion
    ADD CONSTRAINT "ADOPCION_id_animal_fkey" FOREIGN KEY (id_animal) REFERENCES public.animal(id_animal);
 L   ALTER TABLE ONLY public.adopcion DROP CONSTRAINT "ADOPCION_id_animal_fkey";
       public          postgres    false    4697    220    236            n           2606    16632 !   adopcion ADOPCION_id_usuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.adopcion
    ADD CONSTRAINT "ADOPCION_id_usuario_fkey" FOREIGN KEY (id_usuario) REFERENCES public.usuario(id_usuario);
 M   ALTER TABLE ONLY public.adopcion DROP CONSTRAINT "ADOPCION_id_usuario_fkey";
       public          postgres    false    4693    216    236            i           2606    16599 (   visita_juego VISITA_JUEGO_id_animal_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.visita_juego
    ADD CONSTRAINT "VISITA_JUEGO_id_animal_fkey" FOREIGN KEY (id_animal) REFERENCES public.animal(id_animal);
 T   ALTER TABLE ONLY public.visita_juego DROP CONSTRAINT "VISITA_JUEGO_id_animal_fkey";
       public          postgres    false    220    232    4697            j           2606    16589 )   visita_juego VISITA_JUEGO_id_usuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.visita_juego
    ADD CONSTRAINT "VISITA_JUEGO_id_usuario_fkey" FOREIGN KEY (id_usuario) REFERENCES public.usuario(id_usuario);
 U   ALTER TABLE ONLY public.visita_juego DROP CONSTRAINT "VISITA_JUEGO_id_usuario_fkey";
       public          postgres    false    216    4693    232            k           2606    16594 +   visita_juego VISITA_JUEGO_id_visitante_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.visita_juego
    ADD CONSTRAINT "VISITA_JUEGO_id_visitante_fkey" FOREIGN KEY (id_visitante) REFERENCES public.adoptante_visitante(id_adoptante_visitante);
 W   ALTER TABLE ONLY public.visita_juego DROP CONSTRAINT "VISITA_JUEGO_id_visitante_fkey";
       public          postgres    false    224    4701    232            g           2606    16542    VACUNAS_APLCIADAS id_animal    FK CONSTRAINT     �   ALTER TABLE ONLY public."VACUNAS_APLCIADAS"
    ADD CONSTRAINT id_animal FOREIGN KEY (id_animal) REFERENCES public.animal(id_animal);
 G   ALTER TABLE ONLY public."VACUNAS_APLCIADAS" DROP CONSTRAINT id_animal;
       public          postgres    false    227    220    4697            h           2606    16537    VACUNAS_APLCIADAS id_vacuna    FK CONSTRAINT     �   ALTER TABLE ONLY public."VACUNAS_APLCIADAS"
    ADD CONSTRAINT id_vacuna FOREIGN KEY (id_vacuna) REFERENCES public."VACUNA"(id_vacuna);
 G   ALTER TABLE ONLY public."VACUNAS_APLCIADAS" DROP CONSTRAINT id_vacuna;
       public          postgres    false    4699    222    227            f           2606    16476    registro_sesiones usuario    FK CONSTRAINT     �   ALTER TABLE ONLY public.registro_sesiones
    ADD CONSTRAINT usuario FOREIGN KEY (id_usuario) REFERENCES public.usuario(id_usuario);
 C   ALTER TABLE ONLY public.registro_sesiones DROP CONSTRAINT usuario;
       public          postgres    false    4693    216    218                  x������ � �      
      x������ � �            x������ � �            x������ � �         k   x�3�tw��5Q��>�9����NA��Ύ��AA��ƜFz�������'�s�'�d�$*$�e�&�$*T*�f��'r�q���YB�� fg�W� (�         :   x���  �w�P���������]F�]��-�=jF/���Z��+�3{���            x������ � �      �   j  x����n�0E��W��<c�VuC��B��cQ�I�CH@�R���kZ{E���f�;g�����FnX�����r������F�C�B��'R�@V#"����?=����o�c�\�N3	_��U�#�&�<�͖B��n0s������.��#��	i@j�u���[�j)�����ҴBE�f��E�/87d���ˇ~��qYey��� |~7�����\�GwsO��@!���	��b6wW�3(�i��Y�=�0�x��Ӿi��DG�`�f�1~A�(CV$J����4���#q�1�H���s�7W��$��43�
 d�ƛ�ݗ����|����x��(�&!h�f_[���f�f�cX�{��bI�            x������ � �     