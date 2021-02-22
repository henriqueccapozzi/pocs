import Head from 'next/head'

import SiteLogo from '../assets/cv.svg'

import { Container } from 'styles/pages/Home'

const Home: React.FC = () => {
  return (
    <Container>
      <Head>
        <title>Homepage</title>
      </Head>

      <main>
        <SiteLogo />
        <h1>I'm a boilerplate</h1>
      </main>

      <div className="image-credits">
        Ícones feitos por
        <a href="https://www.freepik.com" title="Freepik">Freepik</a>
        from
        <a href="https://www.flaticon.com/br/" title="Flaticon">www.flaticon.com</a>
      </div>
    </Container>
  )
}

export default Home

