import React, { useEffect, useState } from "react";
import { api } from "../../services/api";
import styles from "../styles/Slider.module.css";
import ContentBox from "./ContentBox";

function Slider({ title, page }) {
  const [movies, setMovies] = useState(null);

  useEffect(() => {
    (async () => {
      const response = await api.get(
        `trending/movie/week?api_key=68e356ae11aabb4bf082a0a61801672e&language=en-US&page=${page}`
      );
      const data = response.data.results.slice(0, 6);
      setMovies(data);
    })();
  }, []);

  return (
    <div className={styles.page_body}>
      <h1>{title}</h1>
      <div className={styles.content_box}>
        {movies &&
          movies.map((item, key) => (
            <div key={key}>
              <a href={`/details:id=${item.id}`}>
                <ContentBox
                  banner={`https://image.tmdb.org/t/p/w342/${item.poster_path}`}
                  link={`/details:id=${item.id}`}
                  title=""
                ></ContentBox>
              </a>
            </div>
          ))}
      </div>
    </div>
  );
}

export default Slider;