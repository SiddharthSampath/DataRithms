--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3
-- Dumped by pg_dump version 12.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    category_name character varying NOT NULL,
    category_description character varying NOT NULL
);


ALTER TABLE public.categories OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_seq OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: problems; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.problems (
    id integer NOT NULL,
    question text NOT NULL,
    answer text NOT NULL,
    cat_id integer,
    question_title character varying(80) NOT NULL
);


ALTER TABLE public.problems OWNER TO postgres;

--
-- Name: problems_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.problems_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.problems_id_seq OWNER TO postgres;

--
-- Name: problems_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.problems_id_seq OWNED BY public.problems.id;


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: problems id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.problems ALTER COLUMN id SET DEFAULT nextval('public.problems_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
3b08b50c3288
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categories (id, category_name, category_description) FROM stdin;
6	Strings	Practice all the variations of string problems, ranging from simple problems, like reversing a string, to hard pattern matching problem
7	Hash Table	Use the power of Hash Tables, and the fact that they provide constant access time to your advantage, to bring down that time complexity!
8	Famous Algorithms	Master the most famous algorithms asked in interviews. Learning these will certainly give you a lot of confidence!
1	Arrays	Practice one of the fundamentals of programming, which will help you tackle many more complicated concepts
3	Dynamic Programming	Conquer your fear of the dreaded dynamic programming right here and right now!
2	Linked List	Ever heard of people complaining about reversing a linked list? Learn that and much more right here!
5	Graphs	Okay, I am not going to sugar coat it, Graphs do need quite a bit of practice! Get started now!
4	Greedy Algorithms	You will be using this everywhere once you get the hang of it!
\.


--
-- Data for Name: problems; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.problems (id, question, answer, cat_id, question_title) FROM stdin;
5	<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">Write an efficient program to find the <span style="color: #007020">sum</span> of contiguous subarray within a one<span style="color: #333333">-</span>dimensional array of numbers which has the largest <span style="color: #007020">sum</span><span style="color: #333333">.</span>\r\n\r\nExample\r\nInput\r\n[<span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">13</span>, <span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">3</span>, <span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">25</span>, <span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">20</span>, <span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">3</span>, <span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">16</span>, <span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">23</span>, <span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">12</span>, <span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">5</span>, <span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">22</span>, <span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">15</span>, <span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">4</span>, <span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">7</span>]\r\nOutput\r\n<span style="color: #0000DD; font-weight: bold">7</span>\r\n</pre></div>	<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">kadanesAlgorithm</span>(array):\r\n\tmaxsum <span style="color: #333333">=</span> array[<span style="color: #0000DD; font-weight: bold">0</span>]\r\n\tmaxendinghere <span style="color: #333333">=</span> array[<span style="color: #0000DD; font-weight: bold">0</span>]\r\n\t\r\n\t<span style="color: #008800; font-weight: bold">for</span> num <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(<span style="color: #0000DD; font-weight: bold">1</span>,<span style="color: #007020">len</span>(array)):\r\n\t\tmaxendinghere <span style="color: #333333">=</span> <span style="color: #007020">max</span>(array[num],maxendinghere <span style="color: #333333">+</span> array[num])\r\n\t\tmaxsum <span style="color: #333333">=</span> <span style="color: #007020">max</span>(maxsum,maxendinghere)\r\n\t<span style="color: #008800; font-weight: bold">return</span> maxsum\r\n</pre></div>	1	Kadanes Algorithm
6	<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">You are given an array coordinates, coordinates[i] <span style="color: #333333">=</span> [x, y], where [x, y] represents the coordinate of a point<span style="color: #333333">.</span> Check <span style="color: #008800; font-weight: bold">if</span> these points make a straight line <span style="color: #000000; font-weight: bold">in</span> the XY plane<span style="color: #333333">.</span>\r\n \r\nExample <span style="color: #0000DD; font-weight: bold">1</span>:\r\nInput: coordinates <span style="color: #333333">=</span> [[<span style="color: #0000DD; font-weight: bold">1</span>,<span style="color: #0000DD; font-weight: bold">2</span>],[<span style="color: #0000DD; font-weight: bold">2</span>,<span style="color: #0000DD; font-weight: bold">3</span>],[<span style="color: #0000DD; font-weight: bold">3</span>,<span style="color: #0000DD; font-weight: bold">4</span>],[<span style="color: #0000DD; font-weight: bold">4</span>,<span style="color: #0000DD; font-weight: bold">5</span>],[<span style="color: #0000DD; font-weight: bold">5</span>,<span style="color: #0000DD; font-weight: bold">6</span>],[<span style="color: #0000DD; font-weight: bold">6</span>,<span style="color: #0000DD; font-weight: bold">7</span>]]\r\nOutput: true\r\nExample <span style="color: #0000DD; font-weight: bold">2</span>:\r\nInput: coordinates <span style="color: #333333">=</span> [[<span style="color: #0000DD; font-weight: bold">1</span>,<span style="color: #0000DD; font-weight: bold">1</span>],[<span style="color: #0000DD; font-weight: bold">2</span>,<span style="color: #0000DD; font-weight: bold">2</span>],[<span style="color: #0000DD; font-weight: bold">3</span>,<span style="color: #0000DD; font-weight: bold">4</span>],[<span style="color: #0000DD; font-weight: bold">4</span>,<span style="color: #0000DD; font-weight: bold">5</span>],[<span style="color: #0000DD; font-weight: bold">5</span>,<span style="color: #0000DD; font-weight: bold">6</span>],[<span style="color: #0000DD; font-weight: bold">7</span>,<span style="color: #0000DD; font-weight: bold">7</span>]]\r\nOutput: false\r\n</pre></div>	<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">checkStraightLine</span>(<span style="color: #007020">self</span>, coordinates: List[List[<span style="color: #007020">int</span>]]) <span style="color: #333333">-&gt;</span> <span style="color: #007020">bool</span>:\r\n        <span style="color: #008800; font-weight: bold">if</span> <span style="color: #007020">len</span>(coordinates) <span style="color: #333333">==</span> <span style="color: #0000DD; font-weight: bold">2</span>:\r\n            <span style="color: #008800; font-weight: bold">return</span> <span style="color: #008800; font-weight: bold">True</span>\r\n        \r\n        originX <span style="color: #333333">=</span> coordinates[<span style="color: #0000DD; font-weight: bold">0</span>][<span style="color: #0000DD; font-weight: bold">0</span>]\r\n        originY <span style="color: #333333">=</span> coordinates[<span style="color: #0000DD; font-weight: bold">0</span>][<span style="color: #0000DD; font-weight: bold">1</span>]\r\n        \r\n        <span style="color: #008800; font-weight: bold">if</span> originX <span style="color: #333333">==</span> coordinates[<span style="color: #0000DD; font-weight: bold">1</span>][<span style="color: #0000DD; font-weight: bold">0</span>]:\r\n            slope <span style="color: #333333">=</span> <span style="color: #007020">float</span>(<span style="background-color: #fff0f0">&quot;inf&quot;</span>)\r\n        <span style="color: #008800; font-weight: bold">else</span>:\r\n            slope <span style="color: #333333">=</span> (coordinates[<span style="color: #0000DD; font-weight: bold">1</span>][<span style="color: #0000DD; font-weight: bold">1</span>] <span style="color: #333333">-</span> originY) <span style="color: #333333">/</span> (coordinates[<span style="color: #0000DD; font-weight: bold">1</span>][<span style="color: #0000DD; font-weight: bold">0</span>] <span style="color: #333333">-</span> originX)\r\n        <span style="color: #008800; font-weight: bold">for</span> i <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(<span style="color: #0000DD; font-weight: bold">2</span>, <span style="color: #007020">len</span>(coordinates)):\r\n            y <span style="color: #333333">=</span> coordinates[i][<span style="color: #0000DD; font-weight: bold">1</span>]\r\n            x <span style="color: #333333">=</span> coordinates[i][<span style="color: #0000DD; font-weight: bold">0</span>]\r\n            <span style="color: #008800; font-weight: bold">if</span> x <span style="color: #333333">==</span> originX:\r\n                currentSlope <span style="color: #333333">=</span> <span style="color: #007020">float</span>(<span style="background-color: #fff0f0">&quot;inf&quot;</span>)\r\n            <span style="color: #008800; font-weight: bold">else</span>:\r\n                currentSlope <span style="color: #333333">=</span> (y <span style="color: #333333">-</span> originY) <span style="color: #333333">/</span> (x <span style="color: #333333">-</span> originX)\r\n            <span style="color: #008800; font-weight: bold">if</span> currentSlope <span style="color: #333333">!=</span> slope:\r\n                <span style="color: #008800; font-weight: bold">return</span> <span style="color: #008800; font-weight: bold">False</span>\r\n        <span style="color: #008800; font-weight: bold">return</span> <span style="color: #008800; font-weight: bold">True</span>\r\n</pre></div>	1	Find out if coordinates make a straight line
7	<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">Given two words word1 <span style="color: #000000; font-weight: bold">and</span> word2, find the minimum number of operations required to convert word1 to word2<span style="color: #333333">.</span>\r\nYou have the following <span style="color: #0000DD; font-weight: bold">3</span> operations permitted on a word:\r\nInsert a character\r\nDelete a character\r\nReplace a character\r\nExample <span style="color: #0000DD; font-weight: bold">1</span>:\r\nInput: word1 <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&quot;horse&quot;</span>, word2 <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&quot;ros&quot;</span>\r\nOutput: <span style="color: #0000DD; font-weight: bold">3</span>\r\nExplanation: \r\nhorse <span style="color: #333333">-&gt;</span> rorse (replace h <span style="color: #008800; font-weight: bold">with</span> r)\r\nrorse <span style="color: #333333">-&gt;</span> rose (remove r)\r\nrose <span style="color: #333333">-&gt;</span> ros (remove e)\r\nExample <span style="color: #0000DD; font-weight: bold">2</span>:\r\nInput: word1 <span style="color: #333333">=</span> intention, word2 <span style="color: #333333">=</span> execution\r\nOutput: <span style="color: #0000DD; font-weight: bold">5</span>\r\nExplanation: \r\nintention <span style="color: #333333">-&gt;</span> inention (remove t)\r\ninention <span style="color: #333333">-&gt;</span> enention (replace i <span style="color: #008800; font-weight: bold">with</span> e)\r\nenention <span style="color: #333333">-&gt;</span> exention (replace n <span style="color: #008800; font-weight: bold">with</span> x)\r\nexention <span style="color: #333333">-&gt;</span> exection (replace n <span style="color: #008800; font-weight: bold">with</span> c)\r\nexection <span style="color: #333333">-&gt;</span> execution (insert u)\r\n</pre></div>	<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">minDistance</span>(<span style="color: #007020">self</span>, word1: <span style="color: #007020">str</span>, word2: <span style="color: #007020">str</span>) <span style="color: #333333">-&gt;</span> <span style="color: #007020">int</span>:\r\n        edits <span style="color: #333333">=</span> [[<span style="color: #0000DD; font-weight: bold">0</span> <span style="color: #008800; font-weight: bold">for</span> j <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(<span style="color: #007020">len</span>(word2) <span style="color: #333333">+</span> <span style="color: #0000DD; font-weight: bold">1</span>)] <span style="color: #008800; font-weight: bold">for</span> i <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(<span style="color: #007020">len</span>(word1) <span style="color: #333333">+</span> <span style="color: #0000DD; font-weight: bold">1</span>)]\r\n        \r\n        <span style="color: #008800; font-weight: bold">for</span> i <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(<span style="color: #007020">len</span>(word1) <span style="color: #333333">+</span> <span style="color: #0000DD; font-weight: bold">1</span>):\r\n            <span style="color: #008800; font-weight: bold">for</span> j <span style="color: #000000; font-weight: bold">in</span> <span style="color: #007020">range</span>(<span style="color: #007020">len</span>(word2) <span style="color: #333333">+</span> <span style="color: #0000DD; font-weight: bold">1</span>):\r\n                <span style="color: #008800; font-weight: bold">if</span> i <span style="color: #333333">==</span> <span style="color: #0000DD; font-weight: bold">0</span>:\r\n                    edits[i][j] <span style="color: #333333">=</span> j\r\n                <span style="color: #008800; font-weight: bold">elif</span> j <span style="color: #333333">==</span> <span style="color: #0000DD; font-weight: bold">0</span>:\r\n                    edits[i][j] <span style="color: #333333">=</span> i\r\n                <span style="color: #008800; font-weight: bold">else</span>:\r\n                    <span style="color: #008800; font-weight: bold">if</span> word1[i <span style="color: #333333">-</span> <span style="color: #0000DD; font-weight: bold">1</span>] <span style="color: #333333">==</span> word2[j <span style="color: #333333">-</span> <span style="color: #0000DD; font-weight: bold">1</span>]:\r\n                        edits[i][j] <span style="color: #333333">=</span> edits[i <span style="color: #333333">-</span> <span style="color: #0000DD; font-weight: bold">1</span>][j <span style="color: #333333">-</span> <span style="color: #0000DD; font-weight: bold">1</span>]\r\n                    <span style="color: #008800; font-weight: bold">else</span>:\r\n                        edits[i][j] <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">1</span> <span style="color: #333333">+</span> <span style="color: #007020">min</span>(edits[i <span style="color: #333333">-</span> <span style="color: #0000DD; font-weight: bold">1</span>][j <span style="color: #333333">-</span> <span style="color: #0000DD; font-weight: bold">1</span>], edits[i <span style="color: #333333">-</span> <span style="color: #0000DD; font-weight: bold">1</span>][j], edits[i][j <span style="color: #333333">-</span> <span style="color: #0000DD; font-weight: bold">1</span>])\r\n                    \r\n        <span style="color: #008800; font-weight: bold">return</span> edits[<span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">1</span>][<span style="color: #333333">-</span><span style="color: #0000DD; font-weight: bold">1</span>]\r\n</pre></div>	3	Edit distance
8	<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">You<span style="background-color: #fff0f0">&#39;re given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.</span>\r\nThe letters <span style="color: #000000; font-weight: bold">in</span> J are guaranteed distinct, <span style="color: #000000; font-weight: bold">and</span> <span style="color: #007020">all</span> characters <span style="color: #000000; font-weight: bold">in</span> J <span style="color: #000000; font-weight: bold">and</span> S are letters<span style="color: #333333">.</span> Letters are case sensitive, so <span style="background-color: #fff0f0">&quot;a&quot;</span> <span style="color: #000000; font-weight: bold">is</span> considered a different <span style="color: #007020">type</span> of stone <span style="color: #008800; font-weight: bold">from</span> <span style="background-color: #fff0f0">&quot;A&quot;</span><span style="color: #333333">.</span>\r\nExample <span style="color: #0000DD; font-weight: bold">1</span>:\r\nInput: J <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&quot;aA&quot;</span>, S <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&quot;aAAbbbb&quot;</span>\r\nOutput: <span style="color: #0000DD; font-weight: bold">3</span>\r\nExample <span style="color: #0000DD; font-weight: bold">2</span>:\r\nInput: J <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&quot;z&quot;</span>, S <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&quot;ZZ&quot;</span>\r\nOutput: <span style="color: #0000DD; font-weight: bold">0</span>\r\nNote:\r\nS <span style="color: #000000; font-weight: bold">and</span> J will consist of letters <span style="color: #000000; font-weight: bold">and</span> have length at most <span style="color: #6600EE; font-weight: bold">50.</span>\r\nThe characters <span style="color: #000000; font-weight: bold">in</span> J are distinct<span style="color: #333333">.</span>\r\n</pre></div>	<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">numJewelsInStones</span>(<span style="color: #007020">self</span>, J: <span style="color: #007020">str</span>, S: <span style="color: #007020">str</span>) <span style="color: #333333">-&gt;</span> <span style="color: #007020">int</span>:\r\n        jewelsHash <span style="color: #333333">=</span> {}\r\n        <span style="color: #008800; font-weight: bold">for</span> jewel <span style="color: #000000; font-weight: bold">in</span> J:\r\n            jewelsHash[jewel] <span style="color: #333333">=</span> <span style="color: #008800; font-weight: bold">True</span>\r\n        \r\n        jewels <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">0</span>\r\n        <span style="color: #008800; font-weight: bold">for</span> char <span style="color: #000000; font-weight: bold">in</span> S:\r\n            <span style="color: #008800; font-weight: bold">if</span> char <span style="color: #000000; font-weight: bold">in</span> jewelsHash:\r\n                jewels <span style="color: #333333">+=</span> <span style="color: #0000DD; font-weight: bold">1</span>\r\n        <span style="color: #008800; font-weight: bold">return</span> jewels\r\n</pre></div>	6	Jewels and Stones
4	<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">Write a function which takes <span style="color: #000000; font-weight: bold">in</span> an array, <span style="color: #000000; font-weight: bold">and</span> a target <span style="color: #007020">sum</span>, <span style="color: #000000; font-weight: bold">and</span> <span style="color: #008800; font-weight: bold">if</span> <span style="color: #007020">any</span> two numbers <span style="color: #000000; font-weight: bold">in</span> the array <span style="color: #007020">sum</span> up to the target <span style="color: #007020">sum</span>, the function should <span style="color: #008800; font-weight: bold">return</span> the pair<span style="color: #333333">.</span> If <span style="color: #000000; font-weight: bold">not</span>, it should <span style="color: #008800; font-weight: bold">return</span> []\r\nEx : \r\nInput\r\n[<span style="color: #0000DD; font-weight: bold">1</span>,<span style="color: #0000DD; font-weight: bold">2</span>,<span style="color: #0000DD; font-weight: bold">4</span>,<span style="color: #0000DD; font-weight: bold">6</span>], <span style="color: #0000DD; font-weight: bold">10</span>\r\nOutput\r\n<span style="color: #008800; font-weight: bold">True</span> (<span style="color: #0000DD; font-weight: bold">6</span><span style="color: #333333">+</span><span style="color: #0000DD; font-weight: bold">4</span>)\r\n</pre></div>	<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">twoNumberSum</span>(array, targetSum):\r\n    <span style="color: #888888"># Write your code here.</span>\r\n    complementHash <span style="color: #333333">=</span> {}\r\n\t<span style="color: #008800; font-weight: bold">for</span> num <span style="color: #000000; font-weight: bold">in</span> array:\r\n\t\tcomplement <span style="color: #333333">=</span> targetSum <span style="color: #333333">-</span> num\r\n\t\t<span style="color: #008800; font-weight: bold">if</span> complement <span style="color: #000000; font-weight: bold">in</span> complementHash:\r\n\t\t\t<span style="color: #008800; font-weight: bold">return</span> [num,complement]\r\n\t\t<span style="color: #008800; font-weight: bold">else</span>:\r\n\t\t\tcomplementHash[num] <span style="color: #333333">=</span> <span style="color: #008800; font-weight: bold">True</span>\r\n\t<span style="color: #008800; font-weight: bold">return</span> []\r\n\t\t\r\n</pre></div>	1	Two Number Sum
\.


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categories_id_seq', 8, true);


--
-- Name: problems_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.problems_id_seq', 8, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: problems problems_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.problems
    ADD CONSTRAINT problems_pkey PRIMARY KEY (id);


--
-- Name: problems problems_cat_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.problems
    ADD CONSTRAINT problems_cat_id_fkey FOREIGN KEY (cat_id) REFERENCES public.categories(id);


--
-- PostgreSQL database dump complete
--

